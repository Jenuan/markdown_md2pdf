#!/bin/zsh
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

if [ -d "$PROJECT_ROOT/.venv" ]; then
  source "$PROJECT_ROOT/.venv/bin/activate"
fi

if [ "$#" -eq 0 ]; then
  echo "Arraste arquivo(s) .md ou pasta(s) para este atalho."
  echo
  echo "Exemplo de uso no terminal:"
  echo "  tools/md_para_pdf_drop.command \"docs/Roteiros e produção\""
  echo
  read -r "?Pressione Enter para fechar..."
  exit 1
fi

python3 "$PROJECT_ROOT/tools/md_para_pdf.py" --output "$PROJECT_ROOT/pdfs_dragdrop" --recursive "$@"
exit_code=$?
echo
if [ "$exit_code" -eq 0 ]; then
  echo "PDFs gerados em: $PROJECT_ROOT/pdfs_dragdrop"
else
  echo "Houve erros durante a conversao. Veja as mensagens acima."
fi
echo
read -r "?Pressione Enter para fechar..."
exit "$exit_code"
