# Tapa de UX

Quem nunca ouviu um “dá um tapa no UX”? Uma telinha rápida no fim, como se UX fosse uma demão de tinta. Esta skill é o contrário: regras de UX, cada uma com a sua fonte, para a sua IA revisar aplicativos. Você pede “revisa esse app” ou “revisa essa tela”, e a IA aplica as regras sozinha, sem precisar chamar a skill pelo nome.

*[English version](README.en.md). As regras são as mesmas nas duas línguas; a skill responde na língua em que você escreve.*

## O que tem

70 verificações em 10 assuntos. Cada uma é uma regra que diz o que fazer, por quê, um exemplo errado, um certo e de onde vem.

| Assunto | O que a revisão olha |
|---|---|
| Hierarquia da informação | um estilo por papel de texto, a escala de tamanhos e a régua de espaço |
| Tipografia | família, pesos, tamanho de leitura, entrelinha, alinhamento, maiúsculas, o tom da fonte |
| Acessibilidade | área de toque, contraste, cor, leitor de tela, foco, texto que cresce, movimento |
| Cor | destaque, cores de estado, paleta, cinzas, tema escuro, enfeites, harmonia |
| Botões e ações | botão principal, tipos de botão, nomes, apagar, sair, resposta ao toque |
| Formulários | rótulos, campos necessários, teclado, formatos, erros, ordem, escolhas |
| Estados | tela vazia, espera, erro, sem internet, sucesso, dado que falta |
| UX Writing | consistência de nomes, verbos, voz, mensagens, formatos e escrita |
| Navegação | barra, onde estou, voltar, nomes, caminhos, janelas |
| Psicologia aplicada | leis de Jakob, Hick, Fitts, memória, isolamento, pico e fim, Tesler |

## Instalar no Claude Code

Dentro do Claude Code:

```
/plugin marketplace add othiagopinheiro/tapa-de-ux
/plugin install tapa-de-ux@tapa-de-ux
```

Ou no terminal:

```
claude plugin marketplace add othiagopinheiro/tapa-de-ux
claude plugin install tapa-de-ux@tapa-de-ux
```

Se o seu computador não tem chave SSH cadastrada no GitHub, use o endereço completo no primeiro comando:

```
/plugin marketplace add https://github.com/othiagopinheiro/tapa-de-ux.git
```

Instale uma língua só: `tapa-de-ux` (português) ou `tapa-de-ux-en` (inglês). Com as duas, a mesma revisão apareceria duas vezes.

### Receber as regras novas

Regras novas entram com o tempo. O Claude Code não atualiza sozinho skills de terceiros: ligue uma vez em `/plugin` → Marketplaces → tapa-de-ux → Enable auto-update. Ou atualize na mão:

```
claude plugin marketplace update tapa-de-ux
claude plugin update tapa-de-ux@tapa-de-ux
```

## Usar no Claude (claude.ai)

1. Baixe [dist/tapa-de-ux.zip](dist/tapa-de-ux.zip).
2. No Claude, abra Customize → Skills → “+” → Upload a skill e escolha o ZIP.

Por aqui a regra nova não chega sozinha: baixe o ZIP de novo e envie outra vez.

## Usar em outras ferramentas

A skill segue o padrão aberto [Agent Skills](https://agentskills.io/), que outras ferramentas também leem, como o [Codex](https://learn.chatgpt.com/docs/build-skills), o [Cursor](https://cursor.com/docs/skills), o [GitHub Copilot](https://docs.github.com/en/copilot/concepts/customizations/agent-skills) e o [Gemini CLI](https://geminicli.com/docs/cli/skills/). Nelas:

1. Baixe [dist/tapa-de-ux.zip](dist/tapa-de-ux.zip).
2. Descompacte na pasta `.agents/skills`: a da sua pasta pessoal vale para todos os projetos; a de dentro de um projeto, só para ele. No terminal, para todos os projetos:

   ```
   mkdir -p ~/.agents/skills
   unzip ~/Downloads/tapa-de-ux.zip -d ~/.agents/skills
   ```

3. Abra a ferramenta de novo.

No [Antigravity CLI](https://antigravity.google/docs/skills), a pasta pessoal é outra: `~/.gemini/config/skills`.

Aqui também a regra nova não chega sozinha: apague a pasta `tapa-de-ux`, baixe o ZIP de novo e descompacte. A skill foi testada no Claude. Nas outras ferramentas as regras são as mesmas, mas o jeito de cada uma usar a skill pode variar.

## Como usar

Não precisa chamar os assuntos um por um. Um pedido geral passa pelos 10; para um só, diga qual.

- “Revisa a interface deste app.” — todos os assuntos.
- “Revisa esse print da tela de cadastro.” — todos, só nessa tela.
- “Revisa só a acessibilidade desta tela.” — um assunto.
- “Cria a tela de configurações seguindo as regras de UX.” — as regras entram sem ser citadas.

A revisão vem numa lista só, sem separar por assunto: cada problema com o nome da regra, onde ele está e como fica certo, do que mais atrapalha para o acabamento. Ela propõe e não muda nada sem você pedir. O design system do seu projeto vem antes das regras: se uma regra bater de frente com ele, a revisão segue o projeto e avisa.

Se a skill não entrar sozinha, chame pelo nome: `/tapa-de-ux:tapa-de-ux` no Claude Code; no claude.ai e nas outras ferramentas, “usa a skill tapa-de-ux”.

## Crédito e licença

Regras de Thiago Pinheiro, designer de UX. As leis e os números citados têm a fonte original ao lado de cada regra.

Licença [CC BY 4.0](LICENSE): você pode copiar, adaptar e repassar as regras, inclusive em trabalho pago, desde que dê o crédito a Thiago Pinheiro, aponte a licença e diga o que mudou.
