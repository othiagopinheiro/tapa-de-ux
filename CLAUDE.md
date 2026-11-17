# ux-rules — instruções do projeto

Skill aberta de regras de UX para quem faz aplicativo e quer uma revisão. O Thiago dita as regras; o Claude revisa, escreve no formato e põe na skill. O GitHub é a distribuição: não há site nem deploy.

Quem pede e o estilo da casa estão em `~/.claude/CLAUDE.md`. Regras locais, que não vão a público, estão em `CLAUDE.local.md`.

## O projeto

- **Repositório:** github.com/othiagopinheiro/ux-rules — privado até o Thiago decidir abrir.
- **Grátis e aberta:** sem versão paga (decisão de 17/11/2026), licença CC BY 4.0 — o texto oficial em `LICENSE`, o aviso curto com o crédito em `LICENSE.txt` dentro de cada skill (vai junto no ZIP e em quem copia só a pasta).
- **Formato:** marketplace de plugins do Claude Code. Markdown e JSON, sem build.
- **Quem usa:** quem faz app e quer revisão, no Claude Code (instala pelo marketplace), no claude.ai (sobe o ZIP) ou em outra ferramenta do padrão Agent Skills — Codex, Cursor, Copilot, Gemini CLI —, descompactando o mesmo ZIP em `~/.agents/skills` (conferido nas documentações em 17/11/2026; testada só no Claude).

```
.claude-plugin/marketplace.json        o marketplace (nome: ux-rules), com os dois plugins
plugins/regras-ux/                     o plugin em português (o original)
  .claude-plugin/plugin.json
  skills/regras-ux/SKILL.md            descrição curta + índice dos assuntos
  skills/regras-ux/regras/*.md         um arquivo por assunto, 7 regras cada
plugins/ux-rules/                      o plugin em inglês, adaptado do português
  skills/ux-rules/SKILL.md
  skills/ux-rules/rules/*.md           os mesmos assuntos, na mesma ordem do índice
modelos/regra.md                       o formato de uma regra
dist/regras-ux.zip, dist/ux-rules.zip  as skills para o claude.ai (geradas)
LICENSE                                a CC BY 4.0, texto oficial, sem mudar nada
README.md, README.en.md                a página do repositório nas duas línguas
ferramentas/provar.py                  as provas
ferramentas/gerar-zip.sh               gera o ZIP
```

## Como entra uma regra nova

1. O Thiago dita do jeito que vier. Revise antes de escrever: o que falta, o que conflita com outra regra, o que precisa de número ou fonte. Confira cada número e cada fonte abrindo a página. Mostre a regra escrita e espere o “entra assim”.
2. Escreva no formato de `modelos/regra.md`. Assunto novo é um arquivo novo em `regras/` e uma linha na tabela “Assuntos” do `SKILL.md`, com o “abra quando”.
3. Assunto novo que muda o alcance da skill muda também a `description` do `SKILL.md` (até 200 caracteres, o limite do claude.ai) e a tabela do `README.md`.
4. Leve a regra aprovada para o inglês, no mesmo lugar do arquivo correspondente em `rules/`. Adapte o que é do Brasil — documentos, formatos, moeda, o jeito de tratar a pessoa — e mostre ao Thiago só o que mudou além da tradução. A fonte é a mesma nas duas línguas: fonte nova entra nas duas.
5. Rode `./ferramentas/gerar-zip.sh` e `python3 ferramentas/provar.py`. A prova reprova se o inglês tiver regra, campo ou fonte diferente do português. Rode também as conferências de `CLAUDE.local.md`.
6. Commit em português, com o porquê.

## Regras que não se negociam

1. **Sem “version”** no `plugin.json` nem no `marketplace.json`. Com versão fixa, o push não chega a quem instalou. A prova reprova.
2. **Nada de terceiros sem licença.** Ideia e lei são livres; o texto, os exemplos, a lista e a ordem de um livro ou de outra skill não. Escreva com palavras próprias e cite a fonte original.
3. **Não invente dado.** Número e estudo só com a página aberta e conferida. O que não foi confirmado fica entre [colchetes], e a prova reprova até alguém confirmar.
4. **O português é o original.** A versão em inglês sai do português aprovado, adaptada, e as duas têm as mesmas regras, na mesma ordem e com as mesmas fontes. Mudou uma, muda a outra no mesmo commit.

## Publicação

- Enquanto o repositório for privado, o push só guarda.
- Depois de aberto, todo push chega a quem ligou a atualização automática: pergunte antes de cada push.
- Para abrir: rever o `README.md` e o `README.en.md` e só então `gh repo edit othiagopinheiro/ux-rules --visibility public`.
- Se o repositório mudar de nome, o endereço muda nos dois READMEs e nos dois `LICENSE.txt`.
