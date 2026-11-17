# Formulários

O texto dos campos (16px) está na tipografia (`tipografia.md`), o botão de enviar em botões e ações (`botoes-e-acoes.md`) e o contraste da borda na acessibilidade (`acessibilidade.md`).

**Como revisar (vale para todas as regras):**
1. Preencher o formulário como a pessoa preencheria: com erro, com pressa, colando texto, voltando uma etapa.
2. Para cada campo, perguntar: precisa mesmo? Dá para descobrir sozinho?
3. Errar de propósito e ver onde a mensagem aparece, o que ela diz e se o que foi digitado continua lá.

## Rótulo sempre visível

**Regra:** todo campo tem um rótulo acima dele, que continua visível enquanto a pessoa digita. Texto dentro do campo, que some ao digitar, não faz esse papel; se o campo precisa de um exemplo ou de um formato, ele fica embaixo do rótulo, à vista o tempo todo. No código, o rótulo está ligado ao campo.

**Por quê:** o texto de dentro do campo some quando a pessoa começa a digitar; ela esquece o que o campo pedia e não consegue conferir antes de enviar. E o leitor de tela anuncia um campo sem rótulo só como “campo de texto”.

**Errado:** campos só com “Nome”, “E-mail” e “Telefone” escritos por dentro, sumindo ao digitar.

**Certo:** “E-mail” acima do campo e, logo embaixo, “ex.: nome@exemplo.com”.

**Fontes:** Nielsen Norman Group, “Placeholders in Form Fields Are Harmful” (https://www.nngroup.com/articles/form-design-placeholders/).

## Pedir só o necessário

**Regra:**
- cada campo precisa se justificar;
- o que o app já sabe ou consegue calcular não se pergunta (com a data de nascimento, a idade sai sozinha);
- o que já foi informado não se pede de novo;
- os campos opcionais levam “(opcional)” no rótulo, e os obrigatórios não levam asterisco;
- o cadastro vem depois que a pessoa viu o valor do app, não na abertura.

**Por quê:** cada campo a mais é um motivo para desistir. E o asterisco é um código que a pessoa precisa decifrar; “(opcional)” diz com palavras.

**Errado:** pedir a data de nascimento e, logo depois, a idade; pedir o e-mail duas vezes; exigir conta antes de mostrar qualquer coisa.

**Certo:** só a data de nascimento; “Apelido (opcional)”.

**Fontes:** GOV.UK Design System, Question pages — pedir só o que precisa e marcar o opcional (https://design-system.service.gov.uk/patterns/question-pages/); WCAG 3.3.7, não pedir duas vezes, nível A (https://www.w3.org/WAI/WCAG22/Understanding/redundant-entry.html).

## O teclado e o preenchimento certos

**Regra:** cada campo abre o teclado do que pede — e-mail, número, telefone — e avisa ao aparelho o que é — nome, e-mail, CEP, endereço —, para o celular e o gerenciador de senhas preencherem sozinhos. Colar é sempre permitido, inclusive na senha, e a senha tem a opção de mostrar.

**Por quê:** digitar no celular é lento e cheio de erro. O preenchimento automático poupa tudo isso, e bloquear o colar quebra o gerenciador de senhas.

**Errado:** teclado de letras no campo de CPF; senha que não aceita colar; cadastro em que o celular não sugere nada.

**Certo:** teclado numérico no CPF e no CEP; o celular sugere o e-mail; “Mostrar senha”.

**Fontes:** WCAG 1.3.5, o campo diz o que é, nível AA (https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html); WCAG 3.3.8, colar e gerenciador de senhas, nível AA (https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum.html).

## Aceitar o jeito da pessoa escrever

**Regra:** o campo aceita as variações comuns e arruma sozinho: CPF, telefone e CEP com ou sem pontos, traços e espaços; e-mail com maiúscula ou espaço no fim. Quando um formato é obrigatório, mostre um exemplo no rótulo ou logo abaixo.

**Por quê:** a pessoa digita do jeito dela. Recusar “123.456.789-00” porque o sistema queria só números é erro do app, não dela.

**Errado:** “CPF inválido” para um CPF certo, só porque veio com pontos; data sem dizer o formato.

**Certo:** o CPF aceito de qualquer jeito e mostrado com pontos; “Data de nascimento (ex.: 25/12/1990)”.

**Fontes:** lei de Postel — aceitar com tolerância o que a pessoa digita (https://lawsofux.com/postels-law/); Nielsen Norman Group, explicar o formato pedido (https://www.nngroup.com/articles/web-form-design/).

## Erro perto do campo, dizendo como corrigir

**Regra:**
- quando: depois que a pessoa termina o campo — ao passar para o próximo ou ao enviar —, nunca no meio da digitação nem antes de ela começar;
- onde: logo abaixo do campo, com ícone e texto — a cor sozinha não basta (ver “Nada só por cor”, na acessibilidade);
- o quê: o que está errado e como corrigir;
- com vários erros ao enviar, um resumo no topo e o foco no primeiro;
- nunca apagar o que foi digitado.

**Por quê:** erro longe do campo obriga a procurar. Erro que só diz “inválido” obriga a adivinhar. E erro que apaga tudo faz desistir.

**Exceção:** na criação de senha, as exigências aparecem e vão sendo cumpridas enquanto a pessoa digita — aí a resposta na hora ajuda.

**Errado:** “Erro no formulário” no topo, sem dizer onde; borda vermelha sem texto; reclamar do e-mail no primeiro caractere; a página volta com tudo em branco.

**Certo:** embaixo do CPF, com ícone: “O CPF tem 11 números. Faltam 2.”; e o resto do que foi digitado continua lá.

**Fontes:** Nielsen Norman Group, erro mostrado quando a pessoa termina o campo, e a exceção da senha (https://www.nngroup.com/articles/errors-forms-design-guidelines/) e erro antes da hora (https://www.nngroup.com/articles/hostile-error-messages/); WCAG 3.3.3, sugerir como corrigir, nível AA (https://www.w3.org/WAI/WCAG22/Understanding/error-suggestion.html).

## Uma coluna, na ordem em que a pessoa pensa

**Regra:**
- os campos ficam um embaixo do outro, em uma coluna;
- campos que andam juntos ficam agrupados (endereço, contato);
- a largura do campo sugere o tamanho da resposta: CEP curto, endereço longo;
- a ordem é a da conversa: nome antes de e-mail, endereço antes do horário de entrega;
- formulário longo vira etapas, com “Etapa 2 de 3”.

**Por quê:** numa coluna, o olho desce em linha reta e não pula campo. Em duas, a pessoa não sabe se lê para o lado ou para baixo.

**Exceção:** pares que a pessoa lê como um só — cidade e estado, data e horário — podem ficar lado a lado.

**Errado:** nome e telefone lado a lado e e-mail embaixo do nome; campo de CEP do tamanho do de endereço; vinte campos numa tela só.

**Certo:** uma coluna, endereço agrupado, CEP curto, formulário em etapas curtas.

**Fontes:** Nielsen Norman Group, “Website Forms Usability: Top 10 Recommendations” — uma coluna, campos agrupados e tamanho do campo pela resposta (https://www.nngroup.com/articles/web-form-design/).

## A escolha certa para cada pergunta

**Regra:**
- de duas a cinco opções: todas à vista, para tocar;
- muitas opções: uma lista com busca;
- liga e desliga só para o que muda na hora, como uma configuração;
- quando houver um padrão sensato, ele já vem escolhido;
- consentimento nunca vem marcado.

**Por quê:** opções escondidas num menu de dois toques escondem a decisão. E a caixa “aceito receber ofertas” já marcada decide pela pessoa.

**Errado:** um menu que abre para escolher entre “Sim” e “Não”; uma lista de 200 países sem busca; “Quero receber ofertas” já marcado.

**Certo:** “Sim” e “Não” à vista; país com busca e o Brasil já escolhido; ofertas desmarcado.
