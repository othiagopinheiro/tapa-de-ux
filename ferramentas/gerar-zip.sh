#!/bin/bash
# Gera dist/<skill>.zip para quem usa o claude.ai (Customize > Skills > Upload a skill).
# O "Download ZIP" do GitHub não serve: ele traz o repositório inteiro, e o claude.ai
# precisa da pasta da skill na raiz do ZIP, com o nome igual ao da skill.
# Rode depois de mudar qualquer regra; a prova confere se o ZIP ficou igual à pasta.
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p dist
for skills in plugins/*/skills; do
  for pasta in "$skills"/*/; do
    nome=$(basename "$pasta")
    rm -f "dist/$nome.zip"
    (cd "$skills" && zip -r -X -q "../../../dist/$nome.zip" "$nome" -x '*.DS_Store')
    echo "dist/$nome.zip gerado."
  done
done
