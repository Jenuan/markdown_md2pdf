#!/bin/zsh
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
AUTOMATOR_MODE=app "$SCRIPT_DIR/md_para_pdf_automator.sh" "$@"
exit_code=$?
echo
if [ "$exit_code" -eq 0 ]; then
  echo "PDFs gerados em: $(cd "$SCRIPT_DIR/../.." && pwd)/docs/pdfs_draganddrop"
else
  echo "Houve erros durante a conversao. Veja as mensagens acima."
fi
echo
read -r "?Pressione Enter para fechar..."
exit "$exit_code"
