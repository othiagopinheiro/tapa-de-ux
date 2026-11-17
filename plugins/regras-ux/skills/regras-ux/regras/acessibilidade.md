# Acessibilidade

**Como revisar (vale para todas as regras):**
1. Revisar também o que está escondido: abrir modal, menu e aba inativa antes de medir.
2. Medir o contraste com número, não no olho, e nos dois temas, se houver dois.
3. Só com print, contraste e área de toque saem estimados; nome, ordem e foco não dá para ver num print, e a revisão diz que ficaram de fora.
4. Primeiro o que trava alguém: peça sem nome, contraste abaixo do mínimo, alvo abaixo do piso.

**Exceções (valem para todas as regras):** link no meio de um texto corrido (área de toque); logo e peça desativada (contraste); animação que é essencial ao que a tela faz (movimento).

O título marcado no código e o tamanho mínimo de letra estão na regra de hierarquia (`hierarquia.md`).

## Área de toque

**Regra:** tudo que se toca tem área de pelo menos 44 × 44 no iPhone e na web, e 48 × 48 no Android. O desenho pode ser menor; a área, não. E a área de um alvo não invade a do vizinho.

**Por quê:** dedo não é cursor. Alvo pequeno faz errar o toque, e erra mais quem tem tremor ou usa o celular andando.

**Gravidade:** abaixo da meta é alerta. Abaixo do piso é erro: 28 × 28 pt na Apple, 24 × 24px na WCAG.

**Errado:** um X de 20px sem área em volta; ícones de 24px colados numa barra.

**Certo:** o X desenhado em 20px dentro de uma área de 44; os ícones lado a lado, cada um com 44, sem sobrepor.

**Fontes:** Apple, Accessibility — 44 × 44 pt é o tamanho padrão e 28 × 28 pt o mínimo no iOS e no iPadOS (https://developer.apple.com/design/human-interface-guidelines/accessibility). Android, 48 × 48dp (https://developer.android.com/guide/topics/ui/accessibility/apps). WCAG 2.5.8, 24px, nível AA (https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum), e 2.5.5, 44px, nível AAA (https://www.w3.org/WAI/WCAG22/Understanding/target-size-enhanced).

## Contraste

**Regra:** texto com 4,5:1 sobre o fundo. Texto grande (24px, ou 18,7px em negrito) com 3:1. Ícone, borda de campo e anel de foco com 3:1. A medida vale nos dois temas, sobre o fundo e sobre cada superfície, e inclui o texto de exemplo dentro do campo.

**Por quê:** com pouco contraste, não lê quem enxerga menos, quem tem mais idade ou quem está no sol.

**Errado:** legenda #999 sobre branco (2,85:1); campo com borda #E5E5E5 (1,26:1), que é a única pista de onde ele está.

**Certo:** #767676 é o cinza mais claro que passa sobre branco (4,54:1). Para a borda, #949494 (3,03:1).

**Fontes:** WCAG 1.4.3 (https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) e 1.4.11 (https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html).

## Nada só por cor

**Regra:** estado, erro, alerta e seleção têm ícone ou texto além da cor.

**Por quê:** quem não distingue cores, ou vê a tela com filtro de cor, perde a informação.

**Errado:** campo com erro marcado só pela borda vermelha; aba ativa só com outra cor.

**Certo:** borda vermelha, ícone e a mensagem “Digite um e-mail válido”; aba ativa com cor e peso.

**Fontes:** WCAG 1.4.1 (https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html).

## Cada peça diz o que é

**Regra:** todo controle tem nome, papel e estado que o leitor de tela consegue ler:
- botão só com ícone tem nome (“Fechar”, não “X”);
- imagem que informa tem descrição, e imagem decorativa fica escondida do leitor;
- aba e menu dizem se estão selecionados ou abertos;
- o controle é o nativo: um botão de verdade, não uma caixa que responde ao toque.

**Por quê:** o leitor de tela lê o código, não a tela. Um ícone sem nome vira só “botão”, ou nada.

**Errado:** ícone de lixeira sem nome; uma caixa clicável que não é botão; aba selecionada anunciada igual às outras.

**Certo:** “Excluir filme, botão”; “Meus filmes, aba, selecionada”.

**Fontes:** WCAG 1.1.1 (https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html) e 4.1.2 (https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html).

## Foco visível, na ordem

**Regra:** tudo que é clicável mostra onde está o foco, com contorno de 3:1. O foco, e a leitura do VoiceOver e do TalkBack, anda na mesma ordem em que se lê a tela.

**Por quê:** quem navega por teclado ou por leitor de tela precisa saber onde está. Com a ordem trocada, partes da tela somem.

**Errado:** foco apagado sem nada no lugar; foco que pula do topo para o rodapé e volta.

**Certo:** contorno de 2 a 3px, com um afastamento, na cor de ação; a ordem igual à da tela.

**Fontes:** WCAG 2.4.7 (https://www.w3.org/WAI/WCAG22/Understanding/focus-visible.html) e 2.4.3 (https://www.w3.org/WAI/WCAG22/Understanding/focus-order.html).

## O texto cresce sem quebrar

**Regra:** o app respeita o tamanho de letra escolhido no aparelho — Texto Dinâmico no iPhone, tamanho da fonte no Android, zoom de 200% no navegador — e nada se perde: nem texto cortado, nem texto encavalado, nem rolagem para o lado a partir de 320px.

**Por quê:** quem enxerga menos aumenta a letra do aparelho. Um tamanho travado ignora essa pessoa, e um layout rígido corta o texto dela.

**Errado:** tamanho fixo que ignora a configuração; botão de altura fixa que corta o texto em letra grande.

**Certo:** tamanhos que acompanham a configuração e peças que crescem na altura.

**Fontes:** WCAG 1.4.4, 200% (https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html), e 1.4.10, 320px (https://www.w3.org/WAI/WCAG22/Understanding/reflow.html).

## Movimento sob controle

**Regra:** quando a pessoa pede menos movimento no aparelho, as animações de deslocamento param ou viram um esmaecer simples.

**Por quê:** movimento grande na tela causa enjoo e tontura em quem tem sensibilidade a movimento.

**Errado:** a tela desliza e dá zoom mesmo com “Reduzir movimento” ligado.

**Certo:** com a opção ligada, a troca de tela é sem deslizamento e a rolagem suave fica desligada.

**Fontes:** WCAG 2.3.3, nível AAA (https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html).
