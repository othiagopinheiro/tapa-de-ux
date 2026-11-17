#!/usr/bin/env python3
"""Provas da skill antes de publicar.

Uso:  python3 ferramentas/provar.py

Confere o que quebraria a skill para quem instala, ou faria uma regra chegar
pela metade: os manifestos, o índice, o formato de cada regra, os limites do
claude.ai e se o ZIP está igual à pasta. Diz quantas provas passaram e sai com
erro se alguma falhar.
"""
import json
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
MARKETPLACE = RAIZ / ".claude-plugin" / "marketplace.json"
ZIP_DIR = RAIZ / "dist"

resultados = []  # (passou, nome, detalhe)


def prova(nome, passou, detalhe=""):
    resultados.append((bool(passou), nome, detalhe))


def ler_json(caminho):
    try:
        return json.loads(caminho.read_text(encoding="utf-8")), ""
    except Exception as e:  # o motivo vai para a tela
        return None, str(e)


def tem_versao(obj):
    """Versão fixa faz o push não chegar a quem instalou: a prova reprova."""
    if isinstance(obj, dict):
        return "version" in obj or any(tem_versao(v) for v in obj.values())
    if isinstance(obj, list):
        return any(tem_versao(v) for v in obj)
    return False


def frontmatter(texto):
    m = re.match(r"^---\n(.*?)\n---\n", texto, re.S)
    if not m:
        return {}
    campos = {}
    for linha in m.group(1).splitlines():
        if ":" in linha:
            chave, valor = linha.split(":", 1)
            campos[chave.strip()] = valor.strip()
    return campos


def secoes(texto):
    """Devolve [(titulo, corpo)] das seções '## ' fora de blocos de código."""
    sem_codigo = re.sub(r"```.*?```", "", texto, flags=re.S)
    partes = re.split(r"^## (.+)$", sem_codigo, flags=re.M)
    return [(partes[i].strip(), partes[i + 1]) for i in range(1, len(partes), 2)]


def conferir_skill(pasta_skill, nomes_vistos):
    nome_pasta = pasta_skill.name
    skill_md = pasta_skill / "SKILL.md"
    prova(f"{nome_pasta}: SKILL.md existe", skill_md.exists())
    if not skill_md.exists():
        return
    texto = skill_md.read_text(encoding="utf-8")
    fm = frontmatter(texto)
    nome = fm.get("name", "")
    descricao = fm.get("description", "")
    prova(f"{nome_pasta}: nome no SKILL.md igual ao da pasta", nome == nome_pasta, f"name: {nome!r}")
    prova(f"{nome_pasta}: nome em minúsculas e hífen, até 64 caracteres",
          re.fullmatch(r"[a-z0-9-]{1,64}", nome or "") is not None)
    prova(f"{nome_pasta}: descrição com até 200 caracteres (limite do claude.ai)",
          0 < len(descricao) <= 200, f"{len(descricao)} caracteres")
    linhas = texto.count("\n") + 1
    prova(f"{nome_pasta}: SKILL.md com menos de 500 linhas", linhas < 500, f"{linhas} linhas")

    pasta_regras = pasta_skill / "regras"
    citados = set(re.findall(r"\]\((regras/[^)]+\.md)\)", texto))
    existentes = {f"regras/{p.name}" for p in pasta_regras.glob("*.md")}
    prova(f"{nome_pasta}: todo arquivo citado no índice existe",
          citados <= existentes, ", ".join(sorted(citados - existentes)))
    prova(f"{nome_pasta}: todo arquivo de regras está no índice",
          existentes <= citados, ", ".join(sorted(existentes - citados)))

    obrigatorios = ["**Regra:**", "**Por quê:**", "**Errado:**", "**Certo:**"]
    faltas, pendentes, sem_titulo, links_ruins = [], [], [], []
    total = 0
    for arq in sorted(pasta_regras.glob("*.md")):
        conteudo = arq.read_text(encoding="utf-8")
        if not re.search(r"^# .+", conteudo, re.M):
            sem_titulo.append(arq.name)
        for marca in ("[a confirmar]", "[a definir]"):
            if marca in conteudo:
                pendentes.append(f"{arq.name} ({marca})")
        for url in re.findall(r"\((https?://[^)\s]+)\)", conteudo):
            if not url.startswith("https://"):
                links_ruins.append(f"{arq.name}: {url}")
        for titulo, corpo in secoes(conteudo):
            total += 1
            falta = [c for c in obrigatorios if c not in corpo]
            if falta:
                faltas.append(f"{arq.name} › {titulo}: falta {', '.join(falta)}")
            chave = titulo.lower()
            if chave in nomes_vistos:
                faltas.append(f"{arq.name} › {titulo}: nome repetido (também em {nomes_vistos[chave]})")
            nomes_vistos[chave] = arq.name
    prova(f"{nome_pasta}: todo arquivo de regras tem título", not sem_titulo, ", ".join(sem_titulo))
    prova(f"{nome_pasta}: toda regra tem Regra, Por quê, Errado e Certo, com nome único",
          not faltas, "\n      ".join(faltas))
    prova(f"{nome_pasta}: nenhuma regra com [a confirmar] ou [a definir]", not pendentes, ", ".join(pendentes))
    prova(f"{nome_pasta}: links das fontes em https", not links_ruins, "; ".join(links_ruins))
    prova(f"{nome_pasta}: tem regras", total > 0, f"{total} regras")
    return total


def conferir_zip(pasta_skill):
    """O claude.ai recebe a pasta da skill num ZIP; ele precisa estar igual à pasta."""
    nome = pasta_skill.name
    arq_zip = ZIP_DIR / f"{nome}.zip"
    if not arq_zip.exists():
        prova(f"{nome}: ZIP para o claude.ai existe", False, "rode ./ferramentas/gerar-zip.sh")
        return
    with tempfile.TemporaryDirectory() as tmp, zipfile.ZipFile(arq_zip) as z:
        z.extractall(tmp)
        extraido = Path(tmp) / nome
        def arquivos(base):
            return {str(p.relative_to(base)): p.read_bytes() for p in base.rglob("*")
                    if p.is_file() and p.name != ".DS_Store"}
        no_zip = arquivos(extraido) if extraido.exists() else {}
        na_pasta = arquivos(pasta_skill)
        diferentes = sorted(set(no_zip) ^ set(na_pasta) | {k for k in set(no_zip) & set(na_pasta) if no_zip[k] != na_pasta[k]})
        prova(f"{nome}: ZIP igual à pasta da skill", extraido.exists() and not diferentes,
              "rode ./ferramentas/gerar-zip.sh — difere em: " + ", ".join(diferentes[:5]))


def validar_com_claude():
    claude = shutil.which("claude")
    if not claude:
        prova("claude plugin validate (pulada: claude não instalado)", True)
        return
    r = subprocess.run([claude, "plugin", "validate", str(RAIZ)], capture_output=True, text=True)
    saida = (r.stdout + r.stderr).strip().splitlines()
    prova("claude plugin validate aprova o marketplace", r.returncode == 0, " / ".join(saida[-3:]))


def main():
    dados, erro = ler_json(MARKETPLACE)
    prova("marketplace.json é JSON válido", dados is not None, erro)
    if dados is None:
        return
    prova("marketplace.json tem name, owner e plugins",
          all(k in dados for k in ("name", "owner", "plugins")))
    prova("marketplace.json sem 'version' (senão o push não chega a quem instalou)", not tem_versao(dados))

    nomes_vistos = {}
    for plugin in dados.get("plugins", []):
        nome = plugin.get("name", "?")
        pasta = (RAIZ / plugin.get("source", "")).resolve()
        prova(f"{nome}: pasta do plugin existe", pasta.is_dir(), str(pasta))
        if not pasta.is_dir():
            continue
        pj, erro = ler_json(pasta / ".claude-plugin" / "plugin.json")
        prova(f"{nome}: plugin.json é JSON válido", pj is not None, erro)
        if pj is not None:
            prova(f"{nome}: nome igual no marketplace e no plugin.json", pj.get("name") == nome)
            prova(f"{nome}: plugin.json sem 'version'", not tem_versao(pj))
        for pasta_skill in sorted((pasta / "skills").iterdir()):
            if pasta_skill.is_dir():
                conferir_skill(pasta_skill, {})
                conferir_zip(pasta_skill)
    validar_com_claude()


if __name__ == "__main__":
    main()
    passaram = sum(1 for ok, _, _ in resultados if ok)
    for ok, nome, detalhe in resultados:
        marca = "ok  " if ok else "FALHOU"
        linha = f"  {marca} {nome}"
        if detalhe and (not ok or "caracteres" in detalhe or "linhas" in detalhe or "regras" in detalhe):
            linha += f" — {detalhe}"
        print(linha)
    print(f"\n{passaram} de {len(resultados)} provas passaram.")
    sys.exit(0 if passaram == len(resultados) else 1)
