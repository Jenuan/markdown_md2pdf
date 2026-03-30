#!/usr/bin/env python3
"""
Converte arquivos Markdown (.md) para PDF.

Uso rapido:
  python tools/md_para_pdf.py --input "docs/arquivo.md"
  python tools/md_para_pdf.py --input "docs" --recursive --output "pdfs"
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable, List

import markdown
from fpdf import FPDF
from fpdf.fonts import FontFace, TextStyle


def _monochrome_html_tag_styles() -> dict:
    """Cores neutras (preto) para substituir os defaults coloridos do fpdf2."""
    fam = "ArialUnicode"
    black = "#000000"
    return {
        "a": FontFace(color=black, emphasis="UNDERLINE"),
        "u": FontFace(color=black, emphasis="UNDERLINE"),
        "blockquote": TextStyle(font_family=fam, color=black, t_margin=3, b_margin=3),
        "p": TextStyle(font_family=fam, color=black, t_margin=1.0, b_margin=2.0),
        "h1": TextStyle(
            font_family=fam,
            font_style="B",
            font_size_pt=22,
            color=black,
            t_margin=3.0,
            b_margin=2.5,
        ),
        "h2": TextStyle(
            font_family=fam,
            font_style="B",
            font_size_pt=18,
            color=black,
            t_margin=2.5,
            b_margin=2.0,
        ),
        "h3": TextStyle(
            font_family=fam,
            font_style="B",
            font_size_pt=14,
            color=black,
            t_margin=2.0,
            b_margin=1.8,
        ),
        "h4": TextStyle(
            font_family=fam,
            font_style="B",
            font_size_pt=12,
            color=black,
            t_margin=1.8,
            b_margin=1.5,
        ),
        "h5": TextStyle(
            font_family=fam,
            font_style="B",
            font_size_pt=10,
            color=black,
            t_margin=1.5,
            b_margin=1.2,
        ),
        "h6": TextStyle(
            font_family=fam,
            font_style="B",
            font_size_pt=8,
            color=black,
            t_margin=1.2,
            b_margin=1.0,
        ),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Converte Markdown para PDF (arquivo unico ou lote)."
    )
    parser.add_argument(
        "--input",
        "-i",
        help="Arquivo .md ou pasta de origem.",
    )
    parser.add_argument(
        "paths",
        nargs="*",
        help="Caminhos de arquivos/pastas para conversao (arrastar e soltar).",
    )
    parser.add_argument(
        "--output",
        "-o",
        default="pdfs",
        help="Pasta de destino dos PDFs (padrao: ./pdfs).",
    )
    parser.add_argument(
        "--glob",
        dest="glob_pattern",
        default="*.md",
        help='Padrao de arquivos quando input for pasta (padrao: "*.md").',
    )
    parser.add_argument(
        "--recursive",
        "-r",
        action="store_true",
        help="Busca recursiva ao converter uma pasta.",
    )
    return parser.parse_args()


def wrap_html(content_html: str, title: str) -> str:
    return f"<h1>{title}</h1>\n{content_html}"


def markdown_to_html(md_text: str) -> str:
    return markdown.markdown(
        md_text,
        extensions=[
            "sane_lists",
            "smarty",
            "nl2br",
        ],
    )


def normalize_for_pdf(md_text: str) -> str:
    # Apenas remove variation selector (pode evitar emoji estilizado em algumas fontes).
    # Emojis no texto sao preservados.
    return md_text.replace("\ufe0f", "")


def html_to_pdf(html_content: str, output_pdf: Path) -> bool:
    output_pdf.parent.mkdir(parents=True, exist_ok=True)
    pdf = FPDF(format="A4")
    pdf.set_auto_page_break(auto=True, margin=15)
    # Usa fonte Unicode do macOS para suportar acentos e travessoes.
    unicode_font = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"
    pdf.add_font("ArialUnicode", "", unicode_font)
    pdf.add_font("ArialUnicode", "B", unicode_font)
    pdf.add_font("ArialUnicode", "I", unicode_font)
    pdf.add_font("ArialUnicode", "BI", unicode_font)
    pdf.add_page()
    pdf.set_font("ArialUnicode", size=11)
    pdf.write_html(html_content, tag_styles=_monochrome_html_tag_styles())
    pdf.output(str(output_pdf))
    return True


def build_output_path(source_file: Path, input_root: Path, output_root: Path) -> Path:
    if source_file == input_root:
        return output_root / f"{source_file.stem}.pdf"
    relative = source_file.relative_to(input_root)
    return (output_root / relative).with_suffix(".pdf")


def collect_markdown_files(input_path: Path, glob_pattern: str, recursive: bool) -> List[Path]:
    if input_path.is_file():
        if input_path.suffix.lower() != ".md":
            raise ValueError("O arquivo de entrada precisa ter extensao .md")
        return [input_path]

    if not input_path.is_dir():
        raise ValueError(f"Caminho de entrada nao encontrado: {input_path}")

    iterator: Iterable[Path]
    if recursive:
        iterator = input_path.rglob(glob_pattern)
    else:
        iterator = input_path.glob(glob_pattern)
    return sorted(path for path in iterator if path.is_file() and path.suffix.lower() == ".md")


def collect_from_multiple_inputs(
    raw_paths: List[str], glob_pattern: str, recursive: bool
) -> tuple[List[Path], List[str]]:
    files: set[Path] = set()
    errors: List[str] = []
    for raw_path in raw_paths:
        input_path = Path(raw_path).expanduser().resolve()
        try:
            found = collect_markdown_files(input_path, glob_pattern, recursive)
            files.update(found)
        except ValueError as exc:
            errors.append(f"{input_path}: {exc}")
    return sorted(files), errors


def convert_file(source_file: Path, input_root: Path, output_root: Path) -> tuple[Path, bool, str]:
    try:
        md_text = normalize_for_pdf(source_file.read_text(encoding="utf-8"))
        html_body = markdown_to_html(md_text)
        full_html = wrap_html(html_body, source_file.stem)
        out_pdf = build_output_path(source_file, input_root, output_root)
        ok = html_to_pdf(full_html, out_pdf)
        if not ok:
            return out_pdf, False, "Falha na etapa de geracao do PDF."
        return out_pdf, True, ""
    except Exception as exc:  # noqa: BLE001
        return output_root / f"{source_file.stem}.pdf", False, str(exc)


def main() -> int:
    args = parse_args()
    output_root = Path(args.output).expanduser().resolve()
    all_inputs = [*args.paths]
    if args.input:
        all_inputs.append(args.input)

    if not all_inputs:
        print("Erro: informe --input ou arraste arquivo(s)/pasta(s) para o comando.")
        return 1

    files, input_errors = collect_from_multiple_inputs(
        all_inputs, args.glob_pattern, args.recursive
    )
    for error in input_errors:
        print(f"[ERRO] {error}")

    if not files:
        print("Nenhum arquivo .md encontrado com os criterios informados.")
        return 1
    success_count = 0
    failure_count = 0

    for md_file in files:
        input_root = md_file.parent
        for source in all_inputs:
            source_path = Path(source).expanduser().resolve()
            if source_path.is_dir():
                try:
                    md_file.relative_to(source_path)
                    input_root = source_path
                    break
                except ValueError:
                    continue
        output_pdf, ok, err = convert_file(md_file, input_root, output_root)
        if ok:
            success_count += 1
            print(f"[OK] {md_file} -> {output_pdf}")
        else:
            failure_count += 1
            print(f"[ERRO] {md_file}: {err}")

    total_failures = failure_count + len(input_errors)
    print(f"\nConcluido. Sucessos: {success_count} | Falhas: {total_failures}")
    return 0 if total_failures == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
