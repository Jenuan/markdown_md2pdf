#!/bin/zsh
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
RECURSOS_PY_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
PROJECT_ROOT="$(cd "$RECURSOS_PY_DIR/.." && pwd)"
MODE="${AUTOMATOR_MODE:-quick_action}"

if [ -d "$RECURSOS_PY_DIR/.venv" ]; then
  source "$RECURSOS_PY_DIR/.venv/bin/activate"
fi

if [ "$#" -eq 0 ]; then
  echo "Nenhum item recebido do Automator."
  echo "Selecione arquivo(s) .md ou pasta(s)."
  exit 1
fi

pick_output_dir() {
  local selected_dir
  selected_dir="$(osascript <<'EOF'
try
  POSIX path of (choose folder with prompt "Escolha a pasta de destino dos PDFs")
on error number -128
  return "__CANCELLED__"
end try
EOF
)"
  echo "$selected_dir"
}

run_quick_action() {
  local output_dir
  output_dir="$(pick_output_dir)"
  if [ "$output_dir" = "__CANCELLED__" ]; then
    echo "Operacao cancelada: nenhuma pasta de destino foi escolhida."
    return 1
  fi
  python3 "$SCRIPT_DIR/md_para_pdf.py" --recursive --output "$output_dir" "$@"
}

run_app() {
  local output_dir
  output_dir="$(pick_output_dir)"
  if [ "$output_dir" = "__CANCELLED__" ]; then
    echo "Operacao cancelada: nenhuma pasta de destino foi escolhida."
    return 1
  fi
  python3 "$SCRIPT_DIR/md_para_pdf.py" --recursive --output "$output_dir" "$@"
}

if [ "$MODE" = "app" ]; then
  run_app "$@"
else
  run_quick_action "$@"
fi
