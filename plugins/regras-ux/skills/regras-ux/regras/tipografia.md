# Tipografia

A escala de tamanhos e o título marcado no código estão na hierarquia (`hierarquia.md`). Aqui fica a fonte em si: qual, quantos pesos, em que tamanho, com que respiro e alinhamento.

**Como revisar (vale para todas as regras):**
1. Listar as fontes em uso. No código, pelo nome, pelos arquivos de fonte e pelo tema. Num print, pela categoria — serifada, sem serifa, monoespaçada, manuscrita — e pela família provável, dita como palpite (“parece ser a …”).
2. Procurar as fontes que entraram sem querer. Na web, botão e campo de formulário não herdam a fonte da página e saem na fonte do sistema; e a fonte que não carregou é trocada pela reserva.

## Uma família de fonte

**Regra:** uma família no app inteiro, usando os pesos dela. Se houver uma segunda, ela tem a mesma estrutura — mesmas proporções, mesma altura das minúsculas — e um papel claro, como ficar só nos títulos. Nunca duas fontes quase iguais na mesma tela.

**Por quê:** cada fonte é uma voz. Com várias, a tela parece colagem. Com duas quase iguais, parece que uma falhou ao carregar.

**Errado:** títulos numa fonte, texto em outra e botões numa terceira (a do sistema, sem querer).

**Certo:** uma família em tudo; ou SF Pro Text no texto e SF Pro Display nos títulos, a mesma família da Apple em dois cortes.

## Poucos pesos, e o certo para ler

**Regra:** dois ou três pesos no app, cada um com um papel — por exemplo, regular no texto, seminegrito em títulos e destaques, negrito em números grandes. Texto corrido em regular. Traço fino (light, thin) só em tamanho grande.

**Por quê:** muitos pesos viram ruído e diluem o destaque. Traço fino em letra pequena some, e some mais com pouco contraste ou no sol.

**Errado:** cinco pesos no mesmo app; texto corrido em light de 14px; um parágrafo inteiro em negrito.

**Certo:** regular, seminegrito e negrito, cada um no seu papel.

## Tamanho de leitura

**Regra:** texto corrido com pelo menos 16px na web e no Android, e 17 pt no iPhone. Na web, campo de formulário com menos de 16px faz o iPhone dar zoom na tela quando a pessoa toca nele. Público mais velho pede mais.

**Por quê:** é o tamanho que as próprias plataformas usam no texto principal. Abaixo disso, a leitura longa cansa.

**Errado:** texto corrido em 14px no celular; campo de busca em 14px que dá zoom ao tocar.

**Certo:** texto e campos com 16px ou mais.

**Fontes:** Apple, Body de 17 pt no tamanho padrão (https://developer.apple.com/design/human-interface-guidelines/typography); Material 3, texto grande de 16 (reprodução da escala: https://matraic.github.io/m3e/styles/typography.html).

## Entrelinha e respiro do texto

**Regra:**
- entrelinha de cerca de 1,5 no texto corrido e mais justa nos títulos;
- espaço entre letras original no texto; um pouco aberto em caixa-alta;
- mais espaço entre parágrafos que entre linhas;
- até 80 caracteres por linha;
- o layout aguenta quando a pessoa aumenta esses espaços.

**Por quê:** com entrelinha apertada, as linhas se embolam. Com linha longa, o olho se perde ao voltar para o começo da próxima. E um título com entrelinha de texto parece dois títulos.

**Errado:** parágrafo com entrelinha 1,1; texto ocupando a largura toda do computador; título de duas linhas que parece dois.

**Certo:** texto com 1,5; título com entrelinha justa; linhas de até 80 caracteres.

**Fontes:** WCAG 1.4.8, até 80 caracteres por linha e entrelinha de 1,5, nível AAA (https://www.w3.org/WAI/WCAG22/Understanding/visual-presentation); WCAG 1.4.12, nada se perde quando a pessoa aumenta os espaços do texto, nível AA (https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html).

## Alinhamento do texto

**Regra:**
- texto corrido alinha à esquerda;
- centralizado só em bloco de até duas ou três linhas, como o título e a frase de uma tela vazia ou um aviso breve;
- justificado, nunca;
- um alinhamento só por bloco;
- números em coluna alinham à direita, com algarismos de mesma largura;
- tamanhos diferentes lado a lado alinham pela linha de base, a linha onde as letras se apoiam.

**Por quê:** o olho volta sempre ao mesmo ponto para começar a linha; no centralizado, cada linha começa num lugar, e a leitura cansa a partir da terceira. O justificado abre buracos desiguais entre as palavras, pior no celular, onde cabem poucas palavras por linha. E número à direita põe unidade embaixo de unidade, para comparar de relance.

**Errado:** parágrafo de cinco linhas centralizado; texto justificado no celular; título centralizado e texto à esquerda no mesmo cartão; preços alinhados à esquerda (R$ 9,90 em cima de R$ 120,00); “R$ 25” grande e “/mês” pequeno alinhados pelo topo.

**Certo:** texto corrido à esquerda; centralizado só no título e na frase curta da tela vazia; valores à direita, vírgula embaixo de vírgula; “R$ 25” e “/mês” apoiados na mesma linha.

**Fontes:** WCAG 1.4.8, texto não justificado, nível AAA (https://www.w3.org/WAI/WCAG22/Understanding/visual-presentation).

## Caixa de frase

**Regra:** títulos, botões e menus em caixa de frase: maiúscula só na primeira letra e nos nomes próprios. Caixa-alta só em rótulo curto, de uma ou duas palavras.

**Por quê:** caixa de frase é o jeito como a pessoa lê todo o resto do texto, então flui. Maiúscula em cada palavra quebra a leitura, e caixa-alta em tudo pesa, parece grito e apaga o destaque do que precisa.

**Exceção:** em app em inglês, siga a convenção da plataforma.

**Errado:** “MEUS FILMES” no título; “Ver Todos Os Filmes” no botão.

**Certo:** “Meus filmes”; “Ver todos os filmes”; “NOVO” como rótulo curto.

**Fontes:** Microsoft Writing Style Guide, Capitalization — caixa de frase como padrão (https://learn.microsoft.com/en-us/style-guide/capitalization); Apple, Writing — um estilo de maiúsculas por tipo de elemento, sempre igual (https://developer.apple.com/design/human-interface-guidelines/writing).

## A fonte combina com o produto

**Regra:** a personalidade da fonte combina com o objetivo e o tom do produto. A revisão não decide isso sozinha: identifica a fonte, diz que tom ela passa e pergunta se é esse o tom que o produto quer. Para os textos pequenos da interface — botões, rótulos, números —, a fonte é sempre uma feita para tela.

**Como revisar:**
1. Identificar a fonte: o nome exato pelo código, ou a categoria e o palpite pelo print.
2. Dizer em uma frase o tom que ela passa: tradicional, técnico, amigável, sofisticado, infantil.
3. Se a pessoa não disse o objetivo do produto, perguntar antes de julgar.
4. Se não combinar, sugerir uma ou duas alternativas, sem trocar nada sozinha.

**Por quê:** a fonte fala antes do texto. Uma serifada clássica num app de academia passa um tom antigo, e isso pode ser de propósito ou engano. Só quem faz o produto sabe.

**Errado:** reprovar uma serifada sem perguntar; deixar passar sem comentário uma letra de convite de casamento num app de tarefas do trabalho.

**Certo:** “Os títulos parecem estar na Playfair Display, uma serifada clássica que passa um tom tradicional e sofisticado. É esse o tom do app? Se a ideia é soar moderno e direto, uma sem serifa como a Inter faria isso.”
