# Psicologia aplicada

Leis da psicologia que viram teste na revisão. A ideia de cada lei é de domínio público; o texto daqui é próprio, e a fonte é a pesquisa original. Várias se encontram com outras seções: Fitts com a área de toque (`acessibilidade.md`), isolamento com a cor de destaque (`cor.md`) e o botão principal (`botoes-e-acoes.md`), Jakob com a consistência (`ux-writing.md`), Tesler com formulários (`formularios.md`).

**Como revisar (vale para todas as regras):**
1. Para cada lei, procurar nas telas o que a regra descreve, uma por uma.
2. Na revisão, dizer o nome da lei só quando ajuda a entender o problema; o que importa é o que muda na tela.
3. Lei não é número mágico: nenhuma delas manda ter “no máximo 7 itens” ou “3 cliques”. Se uma revisão chegar a um número assim, é sinal de lei mal aplicada.

## Lei de Jakob

**O que diz:** as pessoas passam a maior parte do tempo em outros apps; por isso esperam que o seu funcione como os que elas já conhecem.

**Regra:** onde existe um jeito conhecido — lupa para buscar, voltar no canto de cima ou no gesto, a conta no canto, puxar a lista para atualizar —, o app segue esse jeito. Inventar só quando o ganho é claro, e aí explicar.

**Por quê:** cada invenção é algo que a pessoa precisa aprender. O que ela já sabe de outros apps é aprendizado de graça.

**Errado:** coração para “salvar para depois” e estrela para “curtir”; a busca escondida dentro do Perfil.

**Certo:** lupa para buscar, coração para curtir; os gestos e os lugares que a plataforma já ensina.

**Fontes:** Jakob Nielsen, “End of Web Design”, 2000 (https://www.nngroup.com/articles/end-of-web-design/).

## Lei de Hick

**O que diz:** quanto mais opções a pessoa precisa comparar, mais ela demora para decidir.

**Regra:** em cada momento, mostrar as opções daquela decisão, com a mais provável em destaque; agrupar ou dividir em etapas as escolhas longas. Não vale esconder o que a pessoa procura: numa lista que ela conhece e que está em ordem — países, contatos —, achar é rápido, e a busca resolve o tamanho.

**Por quê:** doze opções do mesmo peso obrigam a ler todas antes de escolher. Três claras, com uma em destaque, decidem num olhar.

**Errado:** a tela inicial com doze botões iguais; uma lista de trinta configurações sem grupo nenhum.

**Certo:** as três ações mais usadas à vista, a principal em destaque; as configurações agrupadas por assunto, com nomes claros.

**Fontes:** W. E. Hick, “On the rate of gain of information”, Quarterly Journal of Experimental Psychology, 1952; R. Hyman, “Stimulus information as a determinant of reaction time”, Journal of Experimental Psychology, 1953; os limites da lei (https://en.wikipedia.org/wiki/Hick%27s_law).

## Lei de Fitts

**O que diz:** o tempo para acertar um alvo depende da distância até ele e do tamanho dele: perto e grande é rápido; longe e pequeno é lento e erra mais.

**Regra:** a ação mais usada é grande e fica perto de onde a pessoa já está — logo abaixo do último campo, ao lado do item que ela afeta. As ações frequentes vêm primeiro nas listas e menus. E, pela mesma lei ao contrário, a ação que apaga fica longe das comuns, para não ser tocada por engano.

**Por quê:** cada centímetro a mais e cada milímetro a menos custam tempo e erro, toda vez que a pessoa usa o app.

**Errado:** “Excluir” colado em “Salvar”; o botão de enviar pequeno, no canto oposto ao último campo.

**Certo:** “Salvar” largo, logo abaixo do último campo; “Excluir” separado, longe dele.

**Fontes:** Paul M. Fitts, “The information capacity of the human motor system in controlling the amplitude of movement”, Journal of Experimental Psychology, 1954; Nielsen Norman Group, “Fitts's Law and Its Applications in UX” (https://www.nngroup.com/articles/fitts-law/).

## Limite da memória

**O que diz:** a memória de curto prazo guarda poucas coisas ao mesmo tempo, e por pouco tempo — Miller falou em sete, mais ou menos dois, em 1956; estudos depois falam em cerca de quatro blocos. Reconhecer o que está à vista é muito mais fácil que lembrar.

**Regra:** o app não pede para a pessoa lembrar — ele mostra. O que ela precisa da tela anterior continua à vista; as escolhas aparecem resumidas antes de confirmar; o que se compara fica lado a lado; números longos vêm em blocos. O limite não manda cortar menu para sete itens: menu é lido, não decorado.

**Por quê:** cada coisa que a pessoa precisa guardar de cabeça é uma chance de errar ou de voltar para conferir.

**Errado:** a tela pede o código que estava na tela anterior; três planos para comparar, cada um numa tela.

**Certo:** o código continua visível ou é preenchido sozinho; os planos lado a lado; um resumo do pedido antes de confirmar.

**Fontes:** George A. Miller, “The Magical Number Seven, Plus or Minus Two”, Psychological Review, 1956; Nelson Cowan, “The magical number 4 in short-term memory”, Behavioral and Brain Sciences, 2001 (https://en.wikipedia.org/wiki/The_Magical_Number_Seven,_Plus_or_Minus_Two); Nielsen Norman Group, “Short-Term Memory and Web Usability” — inclusive sobre o engano do menu de sete itens (https://www.nngroup.com/articles/short-term-memory-and-web-usability/) e “Memory Recognition and Recall in User Interfaces” (https://www.nngroup.com/articles/recognition-and-recall/).

## Efeito de isolamento

**O que diz:** no meio de coisas parecidas, a que é diferente é a que se nota e se lembra (efeito Von Restorff).

**Regra:** o que mais importa na tela é o único diferente — na cor, no tamanho ou na forma, e não só na cor. Se tudo se diferencia, nada se destaca.

**Por quê:** o destaque funciona por contraste com o resto. Três destaques na mesma tela se anulam.

**Errado:** selos coloridos, banners e um botão laranja disputando a mesma tela; o plano recomendado igual aos outros.

**Certo:** um só elemento diferente por tela — o botão principal, ou o plano recomendado com selo e borda.

**Fontes:** Hedwig von Restorff, “Über die Wirkung von Bereichsbildungen im Spurenfeld”, Psychologische Forschung, 1933 (https://en.wikipedia.org/wiki/Von_Restorff_effect); WCAG 1.4.1, não depender só da cor (https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html).

## Regra do pico e do fim

**O que diz:** a gente julga uma experiência pelo momento mais intenso e pelo fim dela, mais do que pela média.

**Regra:** achar os picos de cada fluxo — o erro no momento mais tenso, o primeiro resultado, o envio do pedido — e caprichar neles e no fim. O fim é desenhado com o mesmo cuidado do começo: fluxo que termina em tela vazia ou em erro seco estraga a lembrança de tudo o que veio antes.

**Por quê:** uma experiência longa e bem feita é lembrada pelo pior momento e pelo fim. Se o fim é seco, é isso que fica.

**Errado:** uma importação longa que termina numa tela vazia; um erro seco bem na hora de enviar o pedido.

**Certo:** “Pronto: seu mapa tem 12 países. Quer incluir o próximo filme?”; no erro, o que houve, o que foi guardado e como seguir.

**Fontes:** Daniel Kahneman, Barbara L. Fredrickson, Charles A. Schreiber e Donald A. Redelmeier, “When More Pain Is Preferred to Less: Adding a Better End”, Psychological Science, 1993; Nielsen Norman Group, “The Peak–End Rule” (https://www.nngroup.com/articles/peak-end-rule/).

## Lei de Tesler

**O que diz:** toda tarefa tem uma parte complicada que não dá para eliminar; dá só para decidir quem lida com ela — o app ou a pessoa (conservação da complexidade).

**Regra:** o app fica com o máximo dessa parte: preenche o que já sabe, calcula o que dá, escolhe um padrão sensato, aceita o formato da pessoa. Simplificar não é esconder: tirar uma opção que a pessoa precisa só passa o trabalho para ela.

**Por quê:** cada coisa que o app deixa para a pessoa fazer, ela faz toda vez. O que o app faz, faz uma vez por todas.

**Errado:** pedir para a pessoa calcular a idade, converter a moeda ou digitar no formato do sistema; “simplificar” tirando o filtro que todo mundo usa.

**Certo:** a idade calculada pela data; o valor convertido na hora; o filtro mais usado à vista, com um padrão já escolhido.

**Fontes:** Larry Tesler, na Xerox PARC, nos anos 1980 — o trabalho com a complexidade deve ficar com quem faz o app, não com quem usa (https://en.wikipedia.org/wiki/Law_of_conservation_of_complexity).
