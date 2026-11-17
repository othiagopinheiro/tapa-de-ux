# UX Writing

Esta seção olha o texto do app como um conjunto: a mesma coisa dita do mesmo jeito em todo lugar. Como na hierarquia, a revisão compara o app inteiro, não uma tela.

O texto do botão está em botões e ações (`botoes-e-acoes.md`), a estrutura do erro e do vazio em estados (`estados.md`) e a caixa de frase na tipografia (`tipografia.md`).

**Como revisar (vale para todas as regras):**
1. Juntar todos os textos do app. No código, os arquivos de texto e de tradução e os textos dentro dos componentes. Num print, o que aparece — e a revisão avisa que vale só para aquelas telas.
2. Montar quatro listas: os nomes das coisas; os verbos das ações; os formatos (data, hora, dinheiro, número); as mensagens por tipo (confirmação, erro, vazio, aviso).
3. Em cada lista, apontar onde a mesma coisa aparece de dois jeitos, com o lugar de cada um.
4. Propor um jeito só e a lista do que muda e onde. Se o projeto já tem um glossário ou um guia de voz, ele vale.

## Cada coisa com um nome só

**Regra:** cada coisa do app — tela, lista, recurso, objeto — tem um nome só, igual no menu, no título, no botão e nas mensagens. O projeto guarda esses nomes numa lista.

**Por quê:** com outro nome, a pessoa acha que é outra coisa, e procura duas vezes.

**Errado:** “Meus filmes” no menu, “Minha lista” no título e “Biblioteca” no aviso; “Ver depois” numa tela e “Favoritos” noutra, para a mesma lista.

**Certo:** “Ver depois” no menu, no título, no botão “Incluir em Ver depois” e no aviso “3 filmes em Ver depois”.

**Fontes:** Apple, Writing — manter uma lista de termos comuns (https://developer.apple.com/design/human-interface-guidelines/writing); Nielsen, heurística 4, consistência e padrões (https://www.nngroup.com/articles/ten-usability-heuristics/).

## Cada ação com um verbo só

**Regra:** a mesma ação usa o mesmo verbo no app inteiro, e verbos diferentes só para resultados diferentes. Se “Arquivar” tira da vista e “Excluir” apaga de vez, essa diferença vale em todas as telas.

**Por quê:** verbo trocado faz a pessoa hesitar (“Gravar é o mesmo que Salvar?”) ou esconde uma diferença que importa: guardar fora da vista ou apagar para sempre.

**Errado:** “Salvar”, “Gravar” e “Guardar” para a mesma ação; “Arquivar” numa tela e “Excluir” noutra, os dois apagando de vez.

**Certo:** “Salvar” em todo lugar; “Arquivar” e “Excluir”, cada um com o seu resultado, sempre.

**Fontes:** Nielsen, heurística 4, consistência e padrões (https://www.nngroup.com/articles/ten-usability-heuristics/); Microsoft Writing Style Guide — não usar um verbo de tirar no sentido de apagar (https://learn.microsoft.com/en-us/style-guide/a-z-word-list-term-collections/r/remove).

## Uma voz no app inteiro

**Regra:** a voz do app é escolhida uma vez e vale em todas as telas: o tratamento da pessoa (em português do Brasil, “você”), o jeito de o app se referir a si mesmo — como “nós” (“Achamos 3 filmes”) ou sem sujeito (“3 filmes encontrados”) — e o grau de formalidade. Se o app já tem uma voz definida, a revisão segue a dele e só aponta onde ela muda.

**Por quê:** voz que muda de tela para tela parece app feito por várias pessoas que não conversaram.

**Errado:** “você” numa tela e “tu” noutra; “Montei sua lista” no meio de “Achamos 3 filmes”; uma tela formal (“Prezado cliente”) e outra cheia de gíria.

**Certo:** a mesma voz do começo ao fim — por exemplo, “Você ainda não tem filmes. Inclua o primeiro e a gente acende o país no mapa.”

**Fontes:** Mailchimp, Voice and Tone — a voz quase não muda; o tom muda o tempo todo (https://styleguide.mailchimp.com/voice-and-tone/); Nielsen, heurística 4 (https://www.nngroup.com/articles/ten-usability-heuristics/).

## Cada tipo de mensagem com um molde só

**Regra:** mensagens do mesmo tipo seguem o mesmo molde no app inteiro. Toda confirmação conta o que mudou, com números; todo erro diz o que houve e o que fazer; todo vazio diz o estado e a saída. O tom se ajusta ao que a pessoa está vivendo naquele momento, mas o mesmo tipo de mensagem tem sempre o mesmo tom.

**Por quê:** quando as mensagens seguem um molde, a pessoa aprende a lê-las de relance. Quando cada uma é de um jeito, toda mensagem vira novidade.

**Errado:** “Filme salvo!”, “Pronto, deu certo 🎉” e “Operação concluída com sucesso” para três confirmações iguais; um erro com piada e outro seco.

**Certo:** “Filme incluído.”, “3 filmes incluídos.”, “Lista apagada.” — sempre o que mudou, curto, com ponto final.

**Fontes:** Mailchimp, Voice and Tone — o tom muda com o estado emocional de quem lê (https://styleguide.mailchimp.com/voice-and-tone/); Nielsen Norman Group, “The Four Dimensions of Tone of Voice” (https://www.nngroup.com/articles/tone-of-voice-dimensions/).

## Cada dado com um formato só

**Regra:** data, hora, dinheiro, número, unidade e telefone são escritos de um jeito só no app inteiro, no padrão do país de quem lê. O plural é tratado: “1 filme”, “5 filmes”, nunca “filme(s)”.

**Por quê:** o mesmo dado em dois formatos faz a pessoa conferir duas vezes, e às vezes ler errado.

**Errado:** “21h00” numa tela e “9:00 PM” noutra; “1 filme(s) incluído(s)”.

**Certo:** um formato escolhido e repetido em todo lugar — por exemplo, “seg, 28 set”, “21:00” e “R$ 4,99”.

**Fontes:** Nielsen, heurística 4 (https://www.nngroup.com/articles/ten-usability-heuristics/); Android, textos com plural (quantity strings) (https://developer.android.com/guide/topics/resources/string-resource).

## Uma escrita só: maiúsculas e pontuação

**Regra:** as mesmas escolhas de escrita no app inteiro: caixa de frase nos títulos e botões (ver tipografia); ponto final em frase completa, não em título, botão nem rótulo; um tipo só de aspas; e emoji, se houver, com a mesma regra em toda parte.

**Por quê:** pontuação e maiúsculas trocadas não impedem a leitura, mas fazem o app parecer remendado.

**Errado:** “Salvar Endereço” num botão e “Salvar endereço” noutro; título com ponto final numa tela e sem noutra; emoji em um aviso e em nenhum outro.

**Certo:** as mesmas escolhas, do primeiro ao último texto.

**Fontes:** Microsoft Writing Style Guide, Periods — ponto em frase completa, nenhum em título e texto de interface (https://learn.microsoft.com/en-us/style-guide/punctuation/periods); Apple, Writing — um estilo de maiúsculas por tipo de elemento (https://developer.apple.com/design/human-interface-guidelines/writing).

## Palavras de quem usa, o importante primeiro

**Regra:** palavras do dia a dia de quem usa o app, sem jargão de sistema (sincronizar, cache, token, erro 500) nem nome interno da empresa (sigla, setor, sistema). A informação que decide vem nas primeiras palavras do título, do item de lista e do aviso; se der para dizer com menos palavras, diga.

**Por quê:** linguagem simples ajuda todo mundo, até especialista. E, na tela, a pessoa passa os olhos: num item de lista, costuma ver só as duas primeiras palavras.

**Errado:** “Falha na sincronização do cache”; “Aqui você encontra as opções para escolher quais avisos quer receber”.

**Certo:** “Não conseguimos atualizar sua lista agora”; “Avisos: escolha quais receber”.

**Fontes:** Nielsen, heurística 2, palavras de quem usa e não jargão interno (https://www.nngroup.com/articles/ten-usability-heuristics/); Nielsen Norman Group, “Plain Language Is for Everyone, Even Experts” (https://www.nngroup.com/articles/plain-language-experts/) e “First 2 Words: A Signal for the Scanning Eye” (https://www.nngroup.com/articles/first-2-words-a-signal-for-scanning/); Apple, Writing — evitar jargão e usar menos palavras (https://developer.apple.com/design/human-interface-guidelines/writing).
