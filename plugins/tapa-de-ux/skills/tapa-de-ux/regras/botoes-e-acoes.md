# Botões e ações

A área de toque está na acessibilidade (`acessibilidade.md`), e a cor de destaque, na cor (`cor.md`).

**Como revisar (vale para todas as regras):**
1. Fazer o inventário de tudo que é clicável: quantos jeitos de botão existem, onde aparece cada um e quantas vezes.
2. Em cada tela, dizer qual é a ação principal e se ela é mesmo a que mais se destaca.
3. Ler o texto de cada botão fora da tela: dá para saber o que acontece?
4. Conferir as ações que apagam e as que demoram: têm desfazer ou confirmação? Mostram que estão carregando?

## Um botão principal por tela

**Regra:** cada tela tem uma ação principal — a que a pessoa veio fazer —, num botão cheio na cor de destaque. As outras ações pesam menos que ela. Ação que apaga nunca é a principal.

**Por quê:** com dois botões iguais lado a lado, a pessoa para para pensar. Com um, ela sabe por onde ir.

**Errado:** “Ver depois” e “Já vi” do mesmo tamanho e cor; “Excluir” em azul cheio, como principal.

**Certo:** “Já vi” cheio, “Ver depois” com contorno, “Não quero” só texto.

**Fontes:** Apple, Buttons — um ou dois botões de destaque por tela, e ação que apaga nunca no papel de principal (https://developer.apple.com/design/human-interface-guidelines/buttons).

## Quatro tipos de botão, poucos tamanhos

**Regra:** quatro tipos, cada um com papel:
- principal: cheio, na cor de destaque;
- secundário: com contorno;
- discreto: só texto, para ação leve ou de saída;
- perigo: vermelho, só para o que apaga.

E poucos tamanhos — por exemplo, grande no rodapé, normal (44) e pequeno (36, dentro de lista, com área de toque em volta). A mesma ação tem a mesma cara no app inteiro.

**Por quê:** cada tipo novo é uma pergunta nova (“isso é mais importante?”). Com quatro, a pessoa aprende o peso de cada ação pela forma.

**Errado:** 17 jeitos de botão no mesmo app; “Ver depois” com uma cara no Início e outra na lista.

**Certo:** quatro tipos e três tamanhos, cada um com uso definido.

## Botão parece botão; etiqueta não

**Regra:** botão tem fundo ou contorno; texto sozinho só para a ação de menor peso. Etiqueta — selo, estado — não tem borda e não é clicável. O que parece clicável é clicável, e o contrário também.

**Por quê:** a pessoa decide onde tocar pela forma. Um botão sem cara de botão nem é visto; uma etiqueta com cara de botão recebe o toque e não faz nada.

**Errado:** “Não quero” cinza-claro sobre cinza-claro, sem borda, parecendo etiqueta; a etiqueta “Só você” com borda, parecendo botão.

**Certo:** ações com fundo ou contorno; etiquetas sem borda e sem toque.

## O botão diz o que faz

**Regra:** o texto do botão é um verbo com o objeto: “Salvar endereço”, “Excluir conta”, “Continuar editando”. Nunca “OK”, “Sim”, “Não” ou “Clique aqui” soltos. Num diálogo, os dois botões dizem o que acontece. A mesma ação tem o mesmo nome no app inteiro.

**Por quê:** muita gente lê só o botão. “Sim” obriga a voltar à pergunta; “Excluir filme” se explica sozinho.

**Exceção:** “OK” num aviso que só informa.

**Errado:** “Tem certeza?” com “Sim” e “Não”; “Salvar” numa tela e “Gravar” na outra.

**Certo:** “Excluir filme” e “Manter filme”.

**Fontes:** Apple, Alerts — verbos nos botões, e “OK” só em aviso que informa (https://developer.apple.com/design/human-interface-guidelines/alerts); Nielsen Norman Group, botões que resumem o que vai acontecer (https://www.nngroup.com/articles/confirmation-dialog/); WCAG 2.4.4, o texto do link diz para onde ele leva, nível A (https://www.w3.org/WAI/WCAG22/Understanding/link-purpose-in-context.html).

## Apagar: desfazer ou confirmar

**Regra:** ação que apaga ou perde algo tem saída.
- Na rotina — tirar um item da lista —, desfazer: um aviso com “Desfazer” por alguns segundos.
- No que é grave e não volta — excluir a conta, apagar tudo —, confirmação: o diálogo diz o que se perde, a ação segura é a principal e a que apaga fica em vermelho, sem destaque.

**Por quê:** confirmação em tudo vira hábito, e a pessoa clica sem ler. Desfazer não interrompe e ainda salva o erro.

**Errado:** “Tem certeza?” a cada item tirado da lista; excluir a conta com um toque, sem volta.

**Certo:** “Filme removido. Desfazer”. E “Excluir sua conta? Seus 120 filmes serão apagados.”, com “Manter conta” como principal e “Excluir conta” em vermelho.

**Fontes:** Nielsen Norman Group, “Confirmation Dialogs Can Prevent User Errors — If Not Overused” (https://www.nngroup.com/articles/confirmation-dialog/); Apple, Alerts (https://developer.apple.com/design/human-interface-guidelines/alerts).

## Sair tão fácil quanto entrar

**Regra:** cancelar, recusar, pular e “Agora não” ficam visíveis, a no máximo dois toques, sem letra miúda nem cor apagada. Quando o app pede consentimento — cookies, notificações, assinatura —, recusar tem o mesmo peso de aceitar.

**Por quê:** esconder a saída prende a pessoa e quebra a confiança no app.

**Errado:** “Não, obrigado, prefiro pagar mais caro” em cinza miúdo; cancelar a assinatura escondido a cinco telas de distância.

**Certo:** “Aceitar” e “Recusar” do mesmo tamanho; “Cancelar assinatura” no Perfil, a dois toques.

**Fontes:** Nielsen, heurística 3, controle e liberdade (https://www.nngroup.com/articles/ten-usability-heuristics/); o “prefiro pagar mais caro” tem nome: confirmshaming (https://www.deceptive.design/types/confirmshaming).

## Toda ação responde

**Regra:**
- o botão muda quando é tocado;
- o que demora mostra “carregando” no próprio botão e não aceita um segundo toque;
- o resultado aparece na tela: o sucesso, curto e dizendo o que mudou (“3 filmes incluídos”), ou a falha real, com o que fazer;
- botão desativado diz o que falta.

**Por quê:** sem resposta, a pessoa toca de novo — e o pedido sai duplicado — ou acha que deu certo quando não deu.

**Errado:** “Salvar” sem retorno nenhum; “Fazer pedido” que aceita dois toques; “Continuar” apagado sem dizer por quê.

**Certo:** “Salvando…” no botão, depois “Endereço salvo.”; “Continuar” ativo, que ao ser tocado mostra o campo que falta.

**Fontes:** Nielsen, heurística 1, o sistema mostra o que está acontecendo (https://www.nngroup.com/articles/ten-usability-heuristics/); Smashing Magazine, “Usability Pitfalls of Disabled Buttons, and How To Avoid Them” (https://www.smashingmagazine.com/2021/08/frustrating-design-patterns-disabled-buttons/).
