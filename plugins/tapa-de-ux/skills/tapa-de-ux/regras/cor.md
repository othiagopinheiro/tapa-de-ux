# Cor

O contraste está na acessibilidade (`acessibilidade.md`), e a regra “nada só por cor” também. Aqui fica o papel de cada cor.

**Como revisar (vale para todas as regras):**
1. Listar todas as cores em uso. No código, cada valor solto e cada variável. Num print, as cores que aparecem, ditas como estimativa.
2. Juntar as quase iguais, as que ninguém distingue lado a lado.
3. Dar a cada cor um papel: fundo, superfície, borda, texto, texto de apoio, destaque, erro, sucesso, aviso. Cor sem papel é candidata a sair.

## Uma cor de destaque

**Regra:** uma cor de destaque por tela, usada no que mais importa — o botão principal, o item ativo. A cor da ação vai só no que se toca: um texto que não é clicável não usa essa cor. A maior parte da tela fica neutra. Como referência, a regra 60-30-10: cerca de 60% neutro, 30% de cor de apoio e 10% de destaque — é guia, não medida.

**Por quê:** destaque em tudo é destaque em nada. E quando a cor da ação aparece num texto comum, a pessoa toca e nada acontece.

**Errado:** laranja no botão, nos ícones, nos títulos e nos selos da mesma tela; um título azul igual aos links, que não é link.

**Certo:** laranja só no botão principal e no item ativo da barra; títulos e ícones em neutro.

**Fontes:** a regra 60-30-10 vem da decoração de interiores e é usada em interface como regra de bolso, sem estudo de tela por trás (https://bootcamp.uxdesign.cc/the-60-30-10-color-rule-for-ui-design-32695d04a7c2).

## Cor de estado tem um significado só

**Regra:** vermelho é erro, perda ou ação que apaga; verde é sucesso; amarelo ou âmbar é aviso. Cor de estado nunca é enfeite, e uma cor não tem dois significados no mesmo app. Se a cor da marca coincide com uma de estado — uma marca vermelha, por exemplo —, o estado ganha ícone e texto para não confundir.

**Por quê:** a pessoa aprende a cor como sinal. Vermelho decorativo parece erro, e verde num botão de excluir convida ao toque errado.

**Errado:** selo vermelho de “Novo”; “Excluir conta” em verde; o mesmo azul para “selecionado” e para “informação”.

**Certo:** “Novo” na cor de destaque ou em neutro; “Excluir conta” em vermelho, com confirmação; cada estado com cor, ícone e texto.

**Fontes:** Apple, Color — evitar a mesma cor para coisas diferentes (https://developer.apple.com/design/human-interface-guidelines/color).

## Uma paleta fechada

**Regra:** toda cor do app sai de uma paleta curta, e cada cor tem um nome pelo papel. Cor solta no código vira cor da paleta ou sai. Cores quase iguais viram uma só.

**Por quê:** três pretos quase iguais não mudam nada para quem vê, mas fazem o app parecer remendado — e cada ajuste futuro precisa ser feito em vários lugares.

**Errado:** 23 cores soltas no código, entre elas #333333, #343434 e #2F2F2F.

**Certo:** uma paleta curta, com nome por papel: fundo, superfície, borda, texto, destaque, erro…

## Poucos cinzas, cada um com papel

**Regra:** texto e texto de apoio bastam na maioria dos apps; um terceiro cinza de texto só se passar 4,5:1. Nenhum cinza mais claro que o último cinza de texto recebe texto — esses ficam para borda, divisor e fundo.

**Por quê:** é no cinza que as paletas incham. Muitos cinzas de texto viram uma hierarquia que ninguém percebe, e os mais claros não passam no contraste.

**Errado:** cinco cinzas de texto, dois abaixo de 4,5:1.

**Certo:** texto e texto de apoio; os outros cinzas só em borda e fundo.

## Os temas valem igual

**Regra:** se o app tem tema claro e escuro, cada cor é redefinida no escuro — não só invertida —, e o contraste é medido de novo nos dois, e no modo de alto contraste quando a plataforma tem. Bloco escuro dentro do tema claro — o topo, um cartão de destaque, um aviso flutuante — troca junto texto, texto pequeno, divisor e erro.

**Por quê:** a cor que funciona sobre branco some sobre preto. O erro mais comum é o bloco escuro herdar o texto escuro e ficar ilegível.

**Errado:** texto de erro vermelho escuro sobre fundo escuro; cartão escuro com o divisor ainda escuro; texto que some no tema escuro porque a cor ficou fixa no código.

**Certo:** cada cor com par claro e escuro, e o contraste conferido nos dois.

**Fontes:** Apple, Color — as cores do app funcionam no claro, no escuro e no alto contraste (https://developer.apple.com/design/human-interface-guidelines/color).

## Sem enfeite

**Regra:** gradiente, sombra e brilho só quando dizem alguma coisa. Sombra é para o que flutua — folha, menu, botão flutuante. O fundo é liso. Se um gradiente parece ser da marca, a revisão pergunta antes de mandar tirar.

**Por quê:** enfeite disputa a atenção com o conteúdo e com o destaque. Sombra em tudo apaga a diferença entre o que flutua e o que está na página.

**Errado:** gradiente roxo e rosa no fundo de toda tela; sombra em todo cartão.

**Certo:** fundo liso; cartão com borda fina; sombra só na folha que sobe.

## Harmonia da paleta

**Regra:** as cores da paleta têm uma relação clara no círculo cromático — análogas (vizinhas, tom calmo), complementares (opostas, contraste forte, boas para o destaque), tríade ou monocromática (um matiz em vários tons). As cores de apoio e de estado têm saturação e luminosidade parecidas com as da marca, e os cinzas puxam levemente para o matiz dela. Duas cores opostas e saturadas nunca ficam uma sobre a outra.

**Como revisar:**
1. Dizer que relação a paleta segue, ou que não segue nenhuma.
2. Apontar a cor que destoa e o par que vibra.
3. Propor o ajuste. A cor da marca não se discute; o resto da paleta se ajusta a ela. Para gerar as opções, o Adobe Color monta paletas por essas relações a partir da cor da marca.

**Por quê:** cores sem relação fazem o app parecer montado aos pedaços. Uma cor de estado gritante rouba a atenção do destaque. E texto vermelho sobre azul cansa a vista e parece tremer, porque as duas cores parecem estar em profundidades diferentes (cromoestereopsia).

**Gravidade:** par que vibra é erro, porque atrapalha a leitura. O resto é sugestão.

**Errado:** marca azul-marinho sóbria com um verde-limão neon de sucesso; texto vermelho puro sobre fundo azul puro; cinzas neutros e frios ao lado de uma marca laranja e quente.

**Certo:** marca azul, laranja (a complementar) só no botão principal, cinzas levemente azulados, e verde e vermelho de estado com a mesma força do azul.

**Fontes:** harmonia de cores (https://en.wikipedia.org/wiki/Color_harmony); vermelho e azul juntos cansam a vista — Susan Weinschenk, “100 Things Every Designer Needs to Know About People”, item 50.
