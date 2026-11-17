# Hierarquia da informação

O texto e o espaço mostram o que é mais importante e o que anda junto. A primeira regra cuida do texto; as seis seguintes, do espaço.

**Como revisar o espaço (vale para as seis regras de espaço):**
1. Medir os espaços de verdade. No código, os valores de margem, respiro e vão. Se der para abrir as telas, medir na largura do menor celular que o app atende. Num print, a medida é estimativa, e a revisão diz isso.
2. Separar os problemas em quatro grupos: alinhamento, agrupamento, repetição e valores fora da régua.
3. Propor a régua e, para cada problema, de quanto para quanto.

**Exceções das regras de espaço:** peças de altura fixa já medidas, como a barra de baixo e o topo; o ajuste óptico (um círculo dentro de uma pílula fica no centro, mesmo fora da régua); o espaço no fim da lista para o botão flutuante não cobrir o último item; selos minúsculos.

## Um estilo por papel

**Regra:** cada texto tem um papel — título, subtítulo, texto ou texto de apoio — e cada papel tem um estilo só, igual no app inteiro. Os tamanhos saem de uma escala, e dois papéis vizinhos ficam a pelo menos um degrau ou um peso de distância. O que aparece como título também é título no código.

**Por quê:** a pessoa lê a tela pela forma antes de ler as palavras. Dois títulos de tamanhos diferentes dizem que um importa mais que o outro, e não importa. Título e texto parecidos escondem onde começa cada parte. E quem usa leitor de tela navega pelos títulos marcados no código: um título que só parece título some para essa pessoa.

**Como revisar:**
1. Levantar os estilos de texto do projeto — fonte, tamanho, peso, altura da linha e cor — e dar a cada um o seu papel.
2. Descobrir se o projeto já tem uma escala: variáveis de tamanho, estilos de texto ou a escala da plataforma. Se tiver e for coerente, ela vale; não troque uma escala que funciona.
3. Apontar:
   - o mesmo papel com estilos diferentes;
   - papéis vizinhos sem um degrau nem um peso de diferença;
   - tamanho fora da escala;
   - texto de apoio abaixo do mínimo da plataforma, quando ela tiver um (no iOS, 11 pt, segundo a Apple);
   - texto com cara de título que, no código, não é título (na web, h1 a h6; em app nativo, a marcação de cabeçalho de acessibilidade), ou títulos fora de ordem.
4. Propor:
   - sem escala, montar uma pela escala modular: base no tamanho do texto e multiplicador 1,25. Com base 16: texto de apoio 13, texto 16, subtítulo 20, título 25. Em app nativo, a escala da plataforma;
   - a tabela com um papel por linha e a lista do que muda e onde.

**Errado:** o título de Perfil em 24px e o de Ajustes em 22px; um subtítulo de 17px ao lado de um texto de 16px, com o mesmo peso; um texto grande e em negrito que, no código, é um parágrafo comum.

**Certo:** todo título de tela igual, todo subtítulo igual, todo texto igual, todo texto de apoio igual; um nível claramente diferente do outro; e o título marcado como título no código.

**Fontes:** escala modular — Tim Brown, “More Meaningful Typography”, A List Apart, 2011 (https://alistapart.com/article/more-meaningful-typography). Tamanhos e mínimo do iOS — Apple, Human Interface Guidelines, Typography (https://developer.apple.com/design/human-interface-guidelines/typography). Título marcado no código — WCAG 1.3.1, nível A (https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships.html).

## Uma régua de espaço

**Regra:** todo espaço sai de uma régua de múltiplos de 4, e cada degrau tem um papel. Se o projeto já tem uma régua coerente, ela vale. Se não tem, propor esta:

| Degrau | Para quê |
|---|---|
| 4 | o texto e a linha de apoio dele (título e ano) |
| 8 | irmãos de um grupo: itens de lista, etiquetas, botões lado a lado, ícone e texto, rótulo e campo |
| 12 | partes de um cartão (imagem e texto); respiro lateral de item de lista |
| 16 | margem da tela no celular; respiro de cartão; entre grupos de uma seção |
| 24 | antes de um título de seção; margem da tela em tablet e computador |
| 32 | entre seções grandes sem linha separando |

**Por quê:** com uma régua, a mesma relação ganha o mesmo espaço em todo lugar. Sem régua aparecem 6, 7, 10 e 14px, diferenças que ninguém percebe, mas que deixam tudo levemente torto.

**Errado:** 6px em 29 lugares, mais 3, 5, 7, 9, 10, 14 e 18px.

**Certo:** só os seis degraus da régua. 1 e 2px só em borda, anel de foco e linha fina.

**Fontes:** grade de 8, com 4 para peças pequenas — Material Design, Layout (https://m2.material.io/design/layout).

## Perto é junto

**Regra:** o espaço dentro de um grupo é sempre menor que o espaço em volta dele. O título de seção fica mais perto do conteúdo dele do que do bloco de cima: 24 em cima, 8 embaixo.

**Por quê:** o olho junta o que está perto antes de ler (lei da proximidade). Espaço igual em tudo deixa a tela sem grupos, e um título longe do próprio conteúdo parece pertencer ao bloco de cima.

**Errado:** um título a 16 do bloco de cima e a 10 da própria lista; um vão de 60px sem motivo.

**Certo:** 24 antes do título, 8 entre o título e a lista, 8 entre os itens.

**Fontes:** Nielsen Norman Group, “Proximity Principle in Visual Design” (https://www.nngroup.com/articles/gestalt-proximity/).

## Uma linha de margem

**Regra:** tudo que se lê ou se toca começa e termina na mesma margem: 16 no celular, 24 em telas maiores. Isso inclui o X de fechar e os botões sobre a imagem.

**Por quê:** a margem é a linha que o olho segue para descer a tela. Uma peça fora dela deixa a tela torta, mesmo que a pessoa não saiba dizer por quê.

**Errado:** o X a 8px da borda e o título a 16; botões sobre a imagem a 12; uma caixa que começa 4px para dentro.

**Certo:** tudo na mesma linha de 16.

**Fontes:** Apple, margens de 16 ou 20 pt conforme o tamanho da tela (https://developer.apple.com/documentation/uikit/positioning-content-within-layout-margins); Material, 16 no celular e 24 a partir do tablet (resumo do SAP Fiori, que segue o Material: https://www.sap.com/design-system/fiori-design-android/v26-4/foundations/adaptive-layout/layout-basics).

## A mesma peça, o mesmo espaço

**Regra:** o componente que se repete tem as mesmas medidas em todo lugar e o mesmo respiro dos dois lados.

**Por quê:** a pessoa reconhece a peça pela forma. Com medidas diferentes, parecem duas peças diferentes, ou um erro.

**Errado:** cartão com 8 de um lado e 12 do outro; etiquetas em quatro tamanhos.

**Certo:** cartão grande com 16 em volta; item de lista com 8 em cima e embaixo e 12 dos lados; um tamanho só de etiqueta.

## Linha ou espaço, não os dois

**Regra:** para separar dois blocos, use uma linha ou um espaço. Nunca as duas coisas, e nunca duas linhas seguidas.

**Por quê:** a linha já separa. Somar outra linha ou um vão grande parece uma seção nova, ou um erro.

**Errado:** abas com a linha delas e, 16px abaixo, outra linha do bloco.

**Certo:** uma linha só, com o mesmo espaço dos dois lados.

## Alinhar pela letra, não pela caixa

**Regra:** o que fica na linha é o que se vê — a letra, o ícone, a estrela —, não a caixa invisível em volta. Um botão só de texto, no começo da linha, é puxado para fora na medida do próprio respiro.

**Por quê:** a caixa não aparece. A pessoa vê o texto 8px para dentro e acha que está desalinhado.

**Errado:** “Não quero” começa 8px depois do título; as estrelas ficam 7px para dentro do rótulo.

**Certo:** o texto do botão começa na mesma linha do título.
