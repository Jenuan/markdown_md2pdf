# Markdown para PDF (md para pdf)

Converta arquivos `.md` em `.pdf` localmente no seu computador usando Python e a biblioteca `fpdf2`.

Se você quer compartilhar textos, roteiros ou conteúdos organizados com tabelas via Google Drive, WhatsApp ou e-mail, este projeto ajuda a transformar seu **Markdown** em **PDF** sem complicação.

## O que este projeto faz

- Lê um ou vários arquivos `.md`
- Converte Markdown para HTML (mantendo listas, quebras de linha e tabelas)
- Gera um arquivo `.pdf` usando `fpdf2`
- Salva o PDF numa pasta de saída (ex.: `docs/pdfs/`)

## Privacidade e segurança

- O processo roda localmente (offline).
- Não usa API keys, tokens ou serviços externos para gerar os PDFs.
- Você só precisa do Python e das dependências listadas em `requirements-md2pdf.txt`.

## Pré-requisitos

1. Ter o **Python 3** instalado
2. Ter o comando `pip` disponível (geralmente vem junto do Python)

## Como instalar (passo a passo no macOS)

1. Abra o terminal e vá para a pasta do projeto `github/`
2. Crie um ambiente virtual (para não misturar dependências):

```bash
python3 -m venv "recursos py/.venv"
source "recursos py/.venv/bin/activate"
pip install -r requirements-md2pdf.txt
```

## Como converter (modo arquivo e modo pasta)

### Converter um arquivo `.md`

```bash
python "recursos py/tools/md_para_pdf.py" --input "example.md" --output "docs/pdfs"
```

### Converter uma pasta (recursivo)

```bash
python "recursos py/tools/md_para_pdf.py" --input "docs" --recursive --output "docs/pdfs"
```

## Usar no macOS sem terminal (arrastar e soltar)

Existe um atalho:

- `recursos py/tools/md_para_pdf_drop.command`

Depois de instalar as dependências (passos acima), você pode:

- Arrastar 1 ou mais arquivos `.md` para esse atalho; ou
- Arrastar uma pasta com arquivos `.md`

Os PDFs gerados ficam em uma pasta de saída dentro de `docs/`.

## Exemplos (para você ver antes de usar)

- `example.md` -> `docs/pdfs/example.pdf`
- `example2.md` -> `docs/pdfs/example2.pdf`

Os exemplos incluem diferentes tipos de título e tabelas para ajudar no resultado final do `md para pdf`.

## Referências e palavras-chave (SEO)

Este projeto é útil para: **converter markdown para pdf**, **md para pdf**, **automator markdown to pdf**, além de aprender como usar `python markdown fpdf2`.

