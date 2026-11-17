# ux-rules

Regras de UX para o Claude revisar aplicativos. Você pede “revisa esse app” ou “revisa essa tela”, e o Claude aplica as regras sozinho, sem precisar chamar a skill pelo nome.

*[English version](README.en.md). As regras são as mesmas nas duas línguas; a skill responde na língua em que você escreve.*

## O que tem

70 regras em 10 assuntos. Cada regra diz o que fazer, por quê, um exemplo errado, um certo e de onde vem.

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
/plugin marketplace add othiagopinheiro/ux-rules
/plugin install regras-ux@ux-rules
```

Ou no terminal:

```
claude plugin marketplace add othiagopinheiro/ux-rules
claude plugin install regras-ux@ux-rules
```

Se o seu computador não tem chave SSH cadastrada no GitHub, use o endereço completo no primeiro comando:

```
/plugin marketplace add https://github.com/othiagopinheiro/ux-rules.git
```

Instale uma língua só: `regras-ux` (português) ou `ux-rules` (inglês). Com as duas, a mesma revisão apareceria duas vezes.

### Receber as regras novas

Regras novas entram com o tempo. O Claude Code não atualiza sozinho skills de terceiros: ligue uma vez em `/plugin` → Marketplaces → ux-rules → Enable auto-update. Ou atualize na mão:

```
claude plugin marketplace update ux-rules
claude plugin update regras-ux@ux-rules
```

## Usar no Claude (claude.ai)

1. Baixe [dist/regras-ux.zip](dist/regras-ux.zip).
2. No Claude, abra Customize → Skills → “+” → Upload a skill e escolha o ZIP.

Por aqui a regra nova não chega sozinha: baixe o ZIP de novo e envie outra vez.

## Como usar

- “Revisa a interface deste app.”
- “Revisa esse print da tela de cadastro.”
- “Cria a tela de configurações seguindo as regras de UX.”

A revisão aponta cada problema com o nome da regra, onde ele está e como fica certo, do que mais atrapalha para o acabamento. Ela propõe e não muda nada sem você pedir. O design system do seu projeto vem antes das regras: se uma regra bater de frente com ele, a revisão segue o projeto e avisa.

## Crédito

Regras de Thiago Pinheiro, designer de UX. As leis e os números citados têm a fonte original ao lado de cada regra.

[licença a decidir antes de abrir o repositório]
