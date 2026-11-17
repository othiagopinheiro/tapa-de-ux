# Modelo de regra

Cada assunto é um arquivo em `plugins/regras-ux/skills/regras-ux/regras/`, com um título (`# Assunto`), um “Como revisar” que vale para o arquivo inteiro e uma seção `## ` por regra. Assunto novo também entra na tabela “Assuntos” do `SKILL.md`.

Copie o bloco abaixo para cada regra. Os campos marcados como obrigatórios são cobrados pela prova (`ferramentas/provar.py`).

```markdown
## Nome curto da regra

**O que diz:** (opcional — para leis e princípios com nome) a ideia em uma frase.

**Regra:** (obrigatório) o que fazer, no presente, em uma a três frases. Lista curta quando houver vários casos.

**Por quê:** (obrigatório) o que acontece com quem usa o app quando a regra é quebrada.

**Como revisar:** (opcional) os passos para achar o problema e propor a correção.

**Gravidade:** (opcional) quando é erro e quando é só sugestão.

**Exceção:** (opcional) quando a regra não vale.

**Errado:** (obrigatório) um exemplo concreto.

**Certo:** (obrigatório) o mesmo exemplo, corrigido.

**Fontes:** (obrigatório quando houver número, estudo ou regra de plataforma) de onde vem, com o endereço.
```

Exemplos sem tema de banco nem de pagamento; prefira filmes, viagens, tarefas, academia.
