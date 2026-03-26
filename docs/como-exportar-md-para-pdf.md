# Export Markdown to PDF (EN) / Como exportar Markdown para PDF (PT)

Este guia mostra como converter `.md` em `.pdf` localmente usando Python e `fpdf2`.

---

## EN: Export Markdown to PDF

### 1) Install dependencies
From the repo root:
```bash
python3 -m venv "recursos py/.venv"
source "recursos py/.venv/bin/activate"
pip install -r requirements-md2pdf.txt
```

### 2) Convert a single file
```bash
python "recursos py/tools/md_para_pdf.py" --input "example.md" --output "docs/pdfs"
```

### 3) Convert a folder (recursive)
```bash
python "recursos py/tools/md_para_pdf.py" --input "docs" --recursive --output "docs/pdfs"
```

### 4) Filter by pattern (glob)
```bash
python "recursos py/tools/md_para_pdf.py" --input "docs" --recursive --glob "*.md" --output "docs/pdfs"
```

### 5) Drag & drop on macOS (no terminal)
Use:
- `recursos py/tools/md_para_pdf_drop.command`

After running the shortcut, it will ask you to choose the destination folder for the PDFs.

### 6) Automator (macOS)
If you prefer a macOS App / Quick Action:
- `docs/como-criar-automator-md-para-pdf.md`

---

## PT: Como exportar Markdown para PDF

Este projeto tem um script Python para converter arquivos `.md` em `.pdf`, ideal para compartilhar no Google Drive ou WhatsApp.

## 1) Instalar dependencias

No terminal, na raiz do projeto:

```bash
python3 -m venv "recursos py/.venv"
source "recursos py/.venv/bin/activate"
pip install -r requirements-md2pdf.txt
```

## 2) Converter um arquivo unico

```bash
python "recursos py/tools/md_para_pdf.py" --input "example.md" --output "docs/pdfs"
```

## 3) Converter varios arquivos da pasta (recursivo)

```bash
python "recursos py/tools/md_para_pdf.py" --input "docs" --recursive --output "docs/pdfs"
```

## 4) Filtrar por padrao (glob)

Todos os `.md`:

```bash
python "recursos py/tools/md_para_pdf.py" --input "docs" --recursive --glob "*.md" --output "docs/pdfs"
```

## Onde os PDFs ficam

Por padrao, o script grava em `docs/pdfs/` (ou na pasta definida em `--output`), mantendo a estrutura de subpastas quando a entrada for uma pasta.

## 5) Usar sem terminal (arrastar e soltar no macOS)

Existe um atalho em `recursos py/tools/md_para_pdf_drop.command`.

### Primeira vez

- Clique com o botao direito no arquivo `.command` e escolha **Abrir**.
- Se o macOS bloquear, permita em **Privacidade e Seguranca** e abra novamente.

### Uso diario

- Arraste 1 ou mais arquivos `.md` para `recursos py/tools/md_para_pdf_drop.command`; ou
- Arraste uma pasta com arquivos `.md`.

O atalho chama automaticamente o conversor e pede para você escolher a pasta de destino dos PDFs.

Tambem e possivel rodar pelo terminal:

```bash
"recursos py/tools/md_para_pdf_drop.command" "example.md"
```

## 6) Automator (mais facil)

Se voce quiser usar como app no Finder e tambem como Acao Rapida (clique direito), siga:

- `docs/como-criar-automator-md-para-pdf.md`

Comportamento atual no Automator:

- App Desktop: pede para escolher a pasta de destino dos PDFs.
- Acao Rapida: tambem pede para escolher a pasta de destino dos PDFs.
