# Create Automator (App + Quick Action) (EN) / Como criar Automator (PT)

This guide creates two macOS shortcuts to convert `.md` files into `.pdf`:
- App (drag & drop)
- Finder Quick Action (right-click)

Both shortcuts use:
- `recursos py/tools/md_para_pdf_automator.sh`

Note: replace `/SEU_CAMINHO_DO_PROJETO/` with the absolute path to this project on your Mac.

macOS-only: Automator and Finder Quick Actions are macOS features and are not available on Windows/Linux.

---

# Como criar Automator (App + Ação Rápida)

Este guia cria dois atalhos no macOS para converter `.md` em `.pdf`:

- Aplicativo (arrastar e soltar)
- Ação Rápida no Finder (clique direito)

Os dois usam o script:

- `recursos py/tools/md_para_pdf_automator.sh`

Somente macOS: Automator e Acoes Rapidas do Finder sao recursos do macOS e nao estao disponiveis em Windows/Linux.

## Preparação

1. Garanta a virtualenv em `recursos py/.venv` com as dependências instaladas.
2. Garanta que os scripts estão executáveis:

```bash
chmod +x "recursos py/tools/md_para_pdf.py" "recursos py/tools/md_para_pdf_automator.sh" "recursos py/tools/md_para_pdf_drop.command"
```

## 1) Criar App no Automator (drag and drop)

1. Abra o **Automator**.
2. Escolha **Aplicativo**.
3. Arraste a ação **Executar Script do Shell**.
4. Configure:
   - Shell: `/bin/zsh`
   - Passar entrada: `como argumentos`
5. Cole este script:

```bash
AUTOMATOR_MODE=app "/SEU_CAMINHO_DO_PROJETO/recursos py/tools/md_para_pdf_automator.sh" "$@"
```

6. Salve como, por exemplo: `MD para PDF.app`.
7. Teste arrastando arquivo(s) `.md` ou pasta(s) para o app.

Saida esperada:

- O app abre um seletor para voce escolher a pasta de destino dos PDFs.
- Se cancelar a selecao, a execucao e encerrada sem gerar arquivos.

## 2) Criar Ação Rápida no Finder

1. Abra o **Automator**.
2. Escolha **Ação Rápida**.
3. No topo:
   - O fluxo de trabalho recebe: `arquivos ou pastas`
   - no: `Finder`
4. Adicione **Executar Script do Shell**.
5. Configure:
   - Shell: `/bin/zsh`
   - Passar entrada: `como argumentos`
6. Cole:

```bash
"/SEU_CAMINHO_DO_PROJETO/recursos py/tools/md_para_pdf_automator.sh" "$@"
```

7. Salve como: `Converter MD para PDF`.

Saida esperada:

- A Ação Rápida abre um seletor para voce escolher a pasta de destino dos PDFs.
- Se cancelar a selecao, a execucao e encerrada sem gerar arquivos.

### Onde aparece (Finder Quick Actions)

- EN: Open Finder, right-click a `.md` file (or a folder with `.md` files), then look under **Quick Actions**.
- PT: Abra o Finder, clique com o botao direito em um arquivo `.md` (ou pasta com `.md`) e veja em **Acoes Rapidas**.

### Se nao aparecer em Quick Actions

- EN: In Automator, confirm the workflow receives `files or folders` in `Finder`.
- PT: No Automator, confirme que o fluxo recebe `arquivos ou pastas` no `Finder`.
- EN: Enable it in `System Settings > Privacy & Security > Extensions > Finder Extensions > Quick Actions` (path may vary by macOS version).
- PT: Habilite em `Ajustes do Sistema > Privacidade e Seguranca > Extensoes > Extensoes do Finder > Acoes Rapidas` (o caminho pode variar por versao do macOS).
- EN/PT: Try right-clicking again and, if needed, restart Finder.

## 3) Permissões no macOS

Se houver bloqueio:

- Va em **Ajustes do Sistema > Privacidade e Seguranca**.
- Permita a execucao do item bloqueado.
- Rode novamente.

## 4) Testes recomendados

- Arquivo unico `.md`
- Pasta com varios `.md`
- Selecao mista (arquivo + pasta) na Ação Rápida

Se nao houver `.md` valido, o script mostra erro e nao gera PDF.
