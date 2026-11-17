# Estados

**Como revisar (vale para todas as regras):**
1. Para cada tela, listar os estados possíveis: vazia na primeira vez, vazia por filtro, carregando, com erro, sem internet, pela metade e cheia demais.
2. Ver se cada estado foi desenhado de propósito ou ficou como saiu do código.
3. No código, forçar cada estado: lista vazia, resposta lenta, servidor fora, internet desligada.

## Toda tela tem todos os estados

**Regra:** cada tela é desenhada nos estados que pode ter, não só no “cheio e funcionando”: vazia, carregando, com erro, sem internet, pela metade e com dado demais.

**Por quê:** a primeira tela que a pessoa vê quase sempre é a vazia, e a pior lembrança costuma ser a do erro. São os estados menos desenhados e os que mais pesam.

**Errado:** a lista que, vazia, mostra só o cabeçalho; o erro que mostra a mensagem crua do servidor.

**Certo:** cada estado com texto, imagem ou ação pensados.

## Tela vazia mostra o caminho

**Regra:** a tela vazia diz que estado é aquele, tem uma frase que acalma e oferece a saída. E muda conforme o motivo:
- primeira vez: o que vai aparecer ali e como começar;
- busca ou filtro sem resultado: qual filtro está ligado, e um botão para limpar;
- tudo feito: a confirmação de que acabou.

**Por quê:** tela em branco parece defeito. Tela vazia bem feita ensina o app e leva à primeira ação.

**Errado:** “Nenhum item.” e nada mais; “Nenhum resultado” sem dizer que o filtro “Só Netflix” está ligado.

**Certo:** “Seu mapa ainda está vazio. Inclua o primeiro filme e veja o país acender.” com o botão “Incluir filme”; “Nada com o filtro Só Netflix.” com “Limpar filtro”.

**Fontes:** Nielsen Norman Group, “Designing Empty States in Complex Applications: 3 Guidelines” (https://www.nngroup.com/articles/empty-state-interface-design/).

## A espera tem a forma certa para o tempo

**Regra:**
- até 1 segundo: nenhum indicador;
- de 1 a 10 segundos: esqueleto — o desenho da página que vai chegar — para a tela inteira, ou o indicador que gira no lugar do que está carregando;
- mais de 10 segundos: progresso de verdade, com etapas nomeadas e números reais crescendo. Nunca uma barra anônima nem um “Carregando…” parado.

E o conteúdo chega no lugar do esqueleto, sem empurrar a tela.

**Por quê:** até 1 segundo, a pessoa não perde o fio. Até 10, ela espera se vê que algo acontece. Passando de 10, precisa saber quanto falta — senão desiste ou acha que travou.

**Errado:** a tela inteira girando por 20 segundos; o texto que pula para baixo quando a imagem carrega.

**Certo:** o esqueleto da lista enquanto carrega; “Buscando seus filmes: 120 de 253” numa importação longa.

**Fontes:** Jakob Nielsen, “Response Times: The 3 Important Limits” (https://www.nngroup.com/articles/response-times-3-important-limits/); Nielsen Norman Group, “Progress Indicators Make a Slow System Less Insufferable” (https://www.nngroup.com/articles/progress-indicators/) e “Skeleton Screens 101” (https://www.nngroup.com/articles/skeleton-screens/).

## Erro diz o que houve e o que fazer

**Regra:** em palavras simples, sem código solto (“Erro 500”) e sem culpar a pessoa, a mensagem diz o que aconteceu, o que continua funcionando e oferece duas saídas: tentar de novo e um caminho alternativo. E não perde o que a pessoa já tinha feito.

**Por quê:** “Algo deu errado” não ajuda a decidir o próximo passo. E culpar a pessoa por uma falha do sistema quebra a confiança.

**Errado:** “Erro 500”; “Você fez algo inválido”; tela de erro sem botão nenhum.

**Certo:** “Não conseguimos buscar o filme agora. O seu mapa continua salvo.” com “Tentar de novo” e “Incluir sem buscar”.

**Fontes:** Nielsen Norman Group, “Error-Message Guidelines” (https://www.nngroup.com/articles/error-message-guidelines/).

## Sem internet, o app continua útil

**Regra:** quando cai a internet, o app diz que o problema é a conexão, mostra o que já tem guardado e segura as ações para enviar depois, avisando. Quando a internet volta, tenta de novo sozinho.

**Por quê:** no celular, a conexão cai no metrô, no elevador, na estrada. App que só mostra erro parece quebrado; app que segura a ação parece confiável.

**Errado:** tela branca com “Falha na rede”; o que a pessoa digitou se perde.

**Certo:** “Sem internet. Seus filmes estão aqui, e o novo vai ser salvo quando a conexão voltar.”

## Sucesso só quando aconteceu

**Regra:** o app só diz que deu certo depois que deu. A mensagem de sucesso conta o que mudou, com números. Se foi pela metade, diz o que entrou e o que não entrou. E se o app mostrou o resultado antes de confirmar e a ação falhou, ele desfaz e avisa.

**Por quê:** sucesso falso é pior que erro: a pessoa só descobre depois, quando já não tem como consertar.

**Errado:** “Importado com sucesso!” quando 7 itens ficaram de fora; o filme que aparece na lista e some ao reabrir o app.

**Certo:** “93 de 100 filmes importados. 7 ficaram de fora: ver quais.”

## Dado que falta não é zero

**Regra:** o que não existe ou não chegou aparece como “—”, não como “0”. Imagem que falta tem um espaço reservado na mesma proporção, honesto sobre não haver foto. E nada de exemplo inventado no app de verdade — nem texto de preenchimento, nem número de mentira.

**Por quê:** “0” é uma informação; “—” é a falta dela. Trocar um pelo outro conta uma mentira, e quem lê toma decisão com base nela.

**Errado:** “0 gols” para um jogo que ainda não aconteceu; “Lorem ipsum” no ar; foto de banco de imagens no lugar da que falta.

**Certo:** “—” no placar do jogo futuro; cartaz cinza com o nome do filme no lugar do pôster que não veio.
