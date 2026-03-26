# Como exportar Markdown para PDF

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
python "recursos py/tools/md_para_pdf.py" --input "docs/Roteiros e produção/[i][vd][corte_mito_01_harpas_anjos_nuvens].md" --output "docs/pdfs"
```

## 3) Converter varios arquivos da pasta (recursivo)

```bash
python "recursos py/tools/md_para_pdf.py" --input "docs/Roteiros e produção" --recursive --output "docs/pdfs"
```

## 4) Filtrar por padrao (glob)

Somente arquivos de Shorts:

```bash
python "recursos py/tools/md_para_pdf.py" --input "docs/Roteiros e produção" --recursive --glob "*shorts*.md" --output "docs/pdfs"
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

O atalho chama automaticamente o conversor e grava os PDFs em `docs/pdfs_draganddrop/`.

Tambem e possivel rodar pelo terminal:

```bash
"recursos py/tools/md_para_pdf_drop.command" "docs/Roteiros e produção"
```

## 6) Automator (mais facil)

Se voce quiser usar como app no Finder e tambem como Acao Rapida (clique direito), siga:

- `docs/como-criar-automator-md-para-pdf.md`

Comportamento atual no Automator:

- App Desktop: pede para escolher a pasta de destino dos PDFs.
- Acao Rapida: tambem pede para escolher a pasta de destino dos PDFs.
