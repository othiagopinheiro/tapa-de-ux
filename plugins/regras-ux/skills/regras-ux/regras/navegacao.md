# Navegação

A área de toque está na acessibilidade (`acessibilidade.md`), e “nada só por cor” também: o item ativo não se marca só pela cor.

**Como revisar (vale para todas as regras):**
1. Desenhar o mapa do app: as seções principais, o que há dentro de cada uma e como se chega a cada tela.
2. Fazer os caminhos mais comuns do começo ao fim e contar os passos. Em cada passo, perguntar: a pessoa sabe onde está e o que vem a seguir?
3. Testar o voltar em cada tela: o botão do app, o gesto do aparelho e o voltar do navegador.

## Navegação à vista

**Regra:** as seções principais ficam numa barra sempre visível — embaixo no celular, em cima ou ao lado no computador —, com três a cinco itens, cada um com ícone e nome. Menu escondido (as três linhas) só quando há seções demais para a barra, e nunca para as principais.

**Por quê:** o que está à vista é usado; o que está escondido é esquecido. E ícone sozinho é adivinhação: poucos ícones são entendidos por todo mundo.

**Errado:** as quatro seções do app dentro de um menu de três linhas; barra só com ícones, sem nome.

**Certo:** barra de baixo com “Mapa”, “Meus filmes”, “Sugestões” e “Perfil”, cada um com ícone e nome.

**Fontes:** Material 3, barra de navegação com três a cinco destinos de mesma importância (https://developer.android.com/develop/ui/compose/components/navigation-bar); Nielsen Norman Group, navegação escondida piora a experiência (https://www.nngroup.com/articles/find-navigation-mobile-even-hamburger/) e ícone precisa de nome ao lado (https://www.nngroup.com/articles/icon-usability/).

## Você está aqui

**Regra:** a pessoa sempre sabe onde está. O item atual da barra fica marcado — por peso, fundo ou forma, além da cor —, e cada tela tem um título próprio, que diz onde ela está.

**Por quê:** sem esse sinal, a pessoa perde o fio, principalmente quando chega por um link ou por uma notificação.

**Errado:** item ativo só um pouco mais escuro; duas telas diferentes com o mesmo título, “Detalhes”.

**Certo:** item ativo com o nome mais pesado e fundo no ícone; “Meus filmes” no título da lista e o nome do filme no título da tela dele.

**Fontes:** Nielsen Norman Group, “Navigation: You Are Here” — destacar o item atual e dar a cada tela um título que a descreva (https://www.nngroup.com/articles/navigation-you-are-here/).

## A barra leva a lugares, não faz ações

**Regra:** cada item da barra é um lugar do app, não uma ação. Ação — incluir, criar, publicar — fica num botão próprio, dentro da tela. A barra é a mesma em todas as telas principais.

**Por quê:** a pessoa usa a barra para se localizar. Um item que abre uma ação em vez de levar a um lugar quebra essa lógica e some com o “onde estou”.

**Errado:** um “+” no meio da barra que abre o formulário de incluir; uma barra que muda de itens de uma tela para outra.

**Certo:** barra só com lugares; “Incluir filme” como botão flutuante nas telas em que faz sentido.

**Fontes:** Apple, Tab bars — a barra serve à navegação, não a ações; escondê-la faz a pessoa esquecer em que parte do app está (https://developer.apple.com/design/human-interface-guidelines/tab-bars); Material 3, a mesma barra em todas as telas principais (https://developer.android.com/develop/ui/compose/components/navigation-bar).

## Voltar sempre funciona

**Regra:** voltar — pelo botão do app, pelo gesto do aparelho ou pelo navegador — leva para onde a pessoa estava, do jeito que estava: a mesma posição na lista, os mesmos filtros, o que ela digitou. Na web, cada tela tem endereço próprio, para o voltar, o recarregar e o compartilhar funcionarem.

**Por quê:** voltar é a saída de emergência. Quando ele perde o lugar, apaga o que foi digitado ou fecha o app, a pessoa passa a ter medo de explorar.

**Errado:** voltar de um filme e cair no topo da lista, sem os filtros; o voltar do navegador sair do app inteiro; recarregar a página e perder a tela.

**Certo:** voltar e encontrar a lista no mesmo ponto, com os filtros ligados.

**Fontes:** Nielsen, heurística 3, uma saída de emergência clara (https://www.nngroup.com/articles/ten-usability-heuristics/); Nielsen Norman Group, a pessoa conta com o voltar para retornar a um lugar conhecido (https://www.nngroup.com/articles/navigation-you-are-here/) e endereços que não mudam, para guardar e voltar (https://www.nngroup.com/articles/url-as-ui/).

## O nome diz o que tem lá

**Regra:** cada item de menu, aba e link antecipa o conteúdo do outro lado, com as palavras de quem usa. Nada de nomes vagos — “Mais”, “Diversos”, “Recursos” — que obrigam a abrir para descobrir.

**Por quê:** a pessoa escolhe o caminho pelo nome. Nome vago faz abrir e voltar, abrir e voltar, até desistir.

**Errado:** “Mais” com metade do app dentro; “Central” sem dizer central de quê.

**Certo:** “Ajuda”, “Configurações”, “Conta”, cada um no seu lugar.

**Fontes:** Nielsen Norman Group, “Information Scent: How Users Decide Where to Go Next” (https://www.nngroup.com/articles/information-scent/).

## Caminho curto para o que mais se faz

**Regra:** as tarefas mais comuns ficam a poucos passos do início, e cada passo mostra que a pessoa está no caminho certo. Não é questão de contar toques: é cada tela deixar claro o próximo passo. O que é raro pode morar mais fundo.

**Por quê:** a tarefa que a pessoa faz todo dia, escondida, vira esforço todo dia. E um passo que não mostra aonde leva faz a pessoa duvidar e voltar.

**Errado:** incluir um filme — a ação mais comum do app — escondido em Perfil, Ajustes, Lista; uma tela no meio do caminho que só tem um botão “Continuar”.

**Certo:** “Incluir filme” a um toque de qualquer tela principal.

**Fontes:** Nielsen Norman Group, “Flat vs. Deep Website Hierarchies” — conteúdo enterrado em muitos níveis é difícil de achar (https://www.nngroup.com/articles/flat-vs-deep-hierarchy/) e “The 3-Click Rule for Navigation Is False” — mais que contar cliques, importa um caminho claro (https://www.nngroup.com/articles/3-click-rule/).

## Janela e folha sabem fechar

**Regra:** toda janela e folha que abre por cima tem um jeito óbvio de fechar: o X (com área de toque), o gesto de puxar para baixo, o voltar do aparelho ou, no computador, o Esc. Folha é para uma escolha rápida sem perder o lugar; tarefa longa vai para uma tela própria. E nunca uma janela por cima de outra.

**Por quê:** janela que não fecha prende. Janela sobre janela faz a pessoa perder o caminho de volta.

**Errado:** folha sem X e sem gesto; uma confirmação que abre por cima de outra janela; formulário longo dentro de uma folha pequena.

**Certo:** folha com puxador, título e X, que fecha ao puxar para baixo; o formulário longo abre em tela cheia.

**Fontes:** Apple, Modality — sempre um jeito óbvio de fechar, e fechar uma janela antes de abrir outra (https://developer.apple.com/design/human-interface-guidelines/modality); W3C, padrão de diálogo — o Esc fecha (https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/).
