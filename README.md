# Markdown to PDF (EN-PT) / md to pdf

## Quick Start (30 seconds) EN + PT

### EN
Convert your `.md` files to `.pdf` locally on your computer using Python and `fpdf2`.

Run:
```bash
python "recursos py/tools/md_para_pdf.py" --input "example.md" --output "docs/pdfs"
```

You will get:
- `docs/pdfs/example.pdf`
- `docs/pdfs/example2.pdf` (from `example2.md`)

### PT
Converta seus arquivos `.md` em `.pdf` localmente no seu computador usando Python e `fpdf2`.

Execute:
```bash
python "recursos py/tools/md_para_pdf.py" --input "example.md" --output "docs/pdfs"
```

Você vai encontrar:
- `docs/pdfs/example.pdf`
- `docs/pdfs/example2.pdf` (a partir de `example2.md`)

## What this project does (EN + PT)

### EN
- Reads one or many `.md` files
- Converts Markdown to HTML (keeps lists, line breaks, and tables)
- Generates a PDF using `fpdf2`
- Saves PDFs to an output folder (for example: `docs/pdfs/`)

### PT
- Lê um ou vários arquivos `.md`
- Converte Markdown para HTML (mantendo listas, quebras de linha e tabelas)
- Gera um arquivo `.pdf` usando `fpdf2`
- Salva o PDF numa pasta de saída (ex.: `docs/pdfs/`)

## How it works (EN + PT)

### EN
Markdown -> HTML -> PDF.

The converter runs offline and only uses your local files and dependencies.

### PT
Markdown -> HTML -> PDF.

O conversor roda offline e usa apenas seus arquivos locais e dependências.

## Install (macOS) (EN + PT)

### EN
From the repo root:
```bash
python3 -m venv "recursos py/.venv"
source "recursos py/.venv/bin/activate"
pip install -r requirements-md2pdf.txt
```

### PT
Na raiz do projeto:
```bash
python3 -m venv "recursos py/.venv"
source "recursos py/.venv/bin/activate"
pip install -r requirements-md2pdf.txt
```

## Convert Markdown to PDF (EN + PT)

### Convert a single file (EN + PT)
```bash
python "recursos py/tools/md_para_pdf.py" --input "example.md" --output "docs/pdfs"
```

### Convert a folder (recursive) (EN + PT)
```bash
python "recursos py/tools/md_para_pdf.py" --input "docs" --recursive --output "docs/pdfs"
```

## Command options (EN + PT)

### EN
- `--recursive`: search `.md` inside a folder
- `--glob`: choose which files match when input is a folder (default: `*.md`)
- `--output`: destination folder for generated PDFs

### PT
- `--recursive`: busca `.md` dentro de uma pasta
- `--glob`: filtra quais arquivos entram quando a entrada é uma pasta (default: `*.md`)
- `--output`: pasta de destino dos PDFs gerados

## macOS: drag & drop (EN + PT)

### EN
Use the shortcut:
- `recursos py/tools/md_para_pdf_drop.command`

After installing dependencies, drag one or more `.md` files (or a folder) onto it.

Generated PDFs go to a folder under `docs/`.

### PT
Use o atalho:
- `recursos py/tools/md_para_pdf_drop.command`

Depois de instalar as dependências, arraste 1 ou mais arquivos `.md` (ou uma pasta) para ele.

Os PDFs gerados ficam em uma pasta dentro de `docs/`.

## Using Automator (macOS)

### EN
If you prefer creating a macOS App / Quick Action, follow:
- [Automator guide (EN)](docs/como-criar-automator-md-para-pdf.md)

### PT
Se você prefere criar um App / Ação Rápida no macOS:
- [Guia do Automator (PT)](docs/como-criar-automator-md-para-pdf.md)

## Examples 

- `example.md` -> `docs/pdfs/example.pdf`
- `example2.md` -> `docs/pdfs/example2.pdf`

These samples include different title levels and tables to show how Markdown turns into PDF.

## FAQ 

### EN
1. Does it require an internet connection or API keys?
   - No. The conversion runs locally (offline) with `python`, `markdown`, and `fpdf2`.
2. How do tables work in the PDF?
   - The converter enables table support during Markdown -> HTML conversion, so tables are rendered into the PDF output.
3. Can I convert a folder of `.md` files?
   - Yes: use `--recursive` and set `--output`.
4. Where are the generated PDFs saved?
   - In the folder you pass in `--output` (default examples use `docs/pdfs/`).

### PT
1. Precisa de internet ou API keys?
   - Não. A conversão roda localmente (offline), usando `python`, `markdown` e `fpdf2`.
2. Tabelas funcionam no PDF?
   - Sim. O conversor habilita suporte a tabelas na etapa Markdown -> HTML, e elas aparecem no PDF.
3. Posso converter uma pasta de `.md`?
   - Sim: use `--recursive` e defina `--output`.
4. Onde os PDFs são salvos?
   - Na pasta definida em `--output` (nos exemplos usamos `docs/pdfs/`).

## Security & Privacy 

### EN
- The process is local/offline.
- No API keys, tokens, or external services are required to generate PDFs.
- If you ever paste tokens/secrets in chats, revoke/rotate them in GitHub and never commit secrets to a public repository.

### PT
- O processo roda localmente (offline).
- Não usa API keys, tokens nem serviços externos para gerar os PDFs.
- Se você compartilhar token/senhas em conversas, revogue/rotate na conta do GitHub e nunca envie segredos para um repositório público.

## Keywords

This repo is useful for: **convert markdown to PDF**, **MD to PDF**, **generate PDF from Markdown**, **markdown to pdf**, **automator markdown to pdf**, and working with **python + fpdf2**.

Também é útil para: **converter markdown para pdf**, **md para pdf**, **automator markdown to pdf** e para aprender `python markdown fpdf2`.

