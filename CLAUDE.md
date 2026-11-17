# ux-rules — instruções do projeto

Skill aberta de regras de UX para quem faz aplicativo e quer uma revisão. O Thiago dita as regras; o Claude revisa, escreve no formato e põe na skill. O GitHub é a distribuição: não há site nem deploy.

Quem pede e o estilo da casa estão em `~/.claude/CLAUDE.md`. Regras locais, que não vão a público, estão em `CLAUDE.local.md`.

## O projeto

- **Repositório:** github.com/othiagopinheiro/ux-rules — privado até o Thiago decidir abrir.
- **Formato:** marketplace de plugins do Claude Code. Markdown e JSON, sem build.
- **Quem usa:** quem faz app e quer revisão, no Claude Code (instala pelo marketplace) ou no claude.ai (sobe o ZIP).

```
.claude-plugin/marketplace.json        o marketplace (nome: ux-rules)
plugins/regras-ux/                     o plugin em português (o original)
  .claude-plugin/plugin.json
  skills/regras-ux/SKILL.md            descrição curta + índice dos assuntos
  skills/regras-ux/regras/*.md         um arquivo por assunto, 7 regras cada
modelos/regra.md                       o formato de uma regra
dist/regras-ux.zip                     a skill para o claude.ai (gerada)
ferramentas/provar.py                  as provas
ferramentas/gerar-zip.sh               gera o ZIP
```

## Como entra uma regra nova

1. O Thiago dita do jeito que vier. Revise antes de escrever: o que falta, o que conflita com outra regra, o que precisa de número ou fonte. Confira cada número e cada fonte abrindo a página. Mostre a regra escrita e espere o “entra assim”.
2. Escreva no formato de `modelos/regra.md`. Assunto novo é um arquivo novo em `regras/` e uma linha na tabela “Assuntos” do `SKILL.md`, com o “abra quando”.
3. Assunto novo que muda o alcance da skill muda também a `description` do `SKILL.md` (até 200 caracteres, o limite do claude.ai) e a tabela do `README.md`.
4. Rode `./ferramentas/gerar-zip.sh` e `python3 ferramentas/provar.py`. Rode também as conferências de `CLAUDE.local.md`.
5. Commit em português, com o porquê.

## Regras que não se negociam

1. **Sem “version”** no `plugin.json` nem no `marketplace.json`. Com versão fixa, o push não chega a quem instalou. A prova reprova.
2. **Nada de terceiros sem licença.** Ideia e lei são livres; o texto, os exemplos, a lista e a ordem de um livro ou de outra skill não. Escreva com palavras próprias e cite a fonte original.
3. **Não invente dado.** Número e estudo só com a página aberta e conferida. O que não foi confirmado fica entre [colchetes], e a prova reprova até alguém confirmar.
4. **O português é o original.** A versão em inglês (quando existir) sai do português aprovado, adaptada, e as duas têm as mesmas regras.

## Publicação

- Enquanto o repositório for privado, o push só guarda.
- Depois de aberto, todo push chega a quem ligou a atualização automática: pergunte antes de cada push.
- Para abrir: decidir a licença, rever o `README.md`, fazer a versão em inglês e só então `gh repo edit othiagopinheiro/ux-rules --visibility public`.
