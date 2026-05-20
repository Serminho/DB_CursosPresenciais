# 📘 Dicionário de Dados

---

## 👤 Entidade Aluno

<table>
<tr>
<th>Atributo</th>
<th>Descrição</th>
<th>Domínio</th>
<th>Restrição do atributo</th>
</tr>

<tr>
<td>id_aluno</td>
<td>Identificador do aluno</td>
<td>INT</td>
<td>Chave Primária (PK)</td>
</tr>

<tr>
<td>nome</td>
<td>Nome completo do aluno</td>
<td>VARCHAR(100)</td>
<td>Não aceita valor nulo</td>
</tr>

<tr>
<td>cpf</td>
<td>CPF do aluno</td>
<td>VARCHAR(14)</td>
<td>Único e não nulo</td>
</tr>

<tr>
<td>email</td>
<td>Email do aluno</td>
<td>VARCHAR(100)</td>
<td>Não aceita valor nulo</td>
</tr>

<tr>
<td>telefone</td>
<td>Telefone do aluno</td>
<td>VARCHAR(15)</td>
<td>Aceita valor nulo</td>
</tr>

<tr>
<td>data_nascimento</td>
<td>Data de nascimento do aluno</td>
<td>DATE</td>
<td>Não aceita valor nulo</td>
</tr>
</table>

---

## 📘 Entidade Curso

<table>
<tr>
<th>Atributo</th>
<th>Descrição</th>
<th>Domínio</th>
<th>Restrição do atributo</th>
</tr>

<tr>
<td>id_curso</td>
<td>Identificador do curso</td>
<td>INT</td>
<td>Chave Primária (PK)</td>
</tr>

<tr>
<td>nome</td>
<td>Nome do curso</td>
<td>VARCHAR(100)</td>
<td>Não aceita valor nulo</td>
</tr>

<tr>
<td>carga_horaria</td>
<td>Carga horária do curso</td>
<td>INT</td>
<td>Não aceita valor nulo</td>
</tr>

<tr>
<td>duracao_meses</td>
<td>Duração em meses</td>
<td>INT</td>
<td>Não aceita valor nulo</td>
</tr>

<tr>
<td>valor</td>
<td>Valor do curso</td>
<td>DECIMAL(10,2)</td>
<td>Não aceita valor nulo</td>
</tr>
</table>

---

## 👨‍🏫 Entidade Professor

<table>
<tr>
<th>Atributo</th>
<th>Descrição</th>
<th>Domínio</th>
<th>Restrição do atributo</th>
</tr>

<tr>
<td>id_professor</td>
<td>Identificador do professor</td>
<td>INT</td>
<td>Chave Primária (PK)</td>
</tr>

<tr>
<td>nome</td>
<td>Nome do professor</td>
<td>VARCHAR(100)</td>
<td>Não aceita valor nulo</td>
</tr>

<tr>
<td>especialidade</td>
<td>Área de especialidade</td>
<td>VARCHAR(100)</td>
<td>Não aceita valor nulo</td>
</tr>

<tr>
<td>email</td>
<td>Email do professor</td>
<td>VARCHAR(100)</td>
<td>Não aceita valor nulo</td>
</tr>

<tr>
<td>telefone</td>
<td>Telefone do professor</td>
<td>VARCHAR(15)</td>
<td>Aceita valor nulo</td>
</tr>
</table>

---

## 🏫 Entidade Turma

<table>
<tr>
<th>Atributo</th>
<th>Descrição</th>
<th>Domínio</th>
<th>Restrição do atributo</th>
</tr>

<tr>
<td>id_turma</td>
<td>Identificador da turma</td>
<td>INT</td>
<td>Chave Primária (PK)</td>
</tr>

<tr>
<td>nome_turma</td>
<td>Nome da turma</td>
<td>VARCHAR(50)</td>
<td>Não aceita valor nulo</td>
</tr>

<tr>
<td>turno</td>
<td>Turno da turma</td>
<td>VARCHAR(20)</td>
<td>Não aceita valor nulo</td>
</tr>

<tr>
<td>semestre</td>
<td>Semestre da turma</td>
<td>VARCHAR(20)</td>
<td>Não aceita valor nulo</td>
</tr>
</table>

---

## 📝 Entidade Matricula

<table>
<tr>
<th>Atributo</th>
<th>Descrição</th>
<th>Domínio</th>
<th>Restrição do atributo</th>
</tr>

<tr>
<td>id_matricula</td>
<td>Identificador da matrícula</td>
<td>INT</td>
<td>Chave Primária (PK)</td>
</tr>

<tr>
<td>data_matricula</td>
<td>Data da matrícula</td>
<td>DATE</td>
<td>Não aceita valor nulo</td>
</tr>

<tr>
<td>status</td>
<td>Status da matrícula</td>
<td>VARCHAR(20)</td>
<td>Não aceita valor nulo</td>
</tr>
</table>

---

## 📚 Entidade Disciplina

<table>
<tr>
<th>Atributo</th>
<th>Descrição</th>
<th>Domínio</th>
<th>Restrição do atributo</th>
</tr>

<tr>
<td>id_disciplina</td>
<td>Identificador da disciplina</td>
<td>INT</td>
<td>Chave Primária (PK)</td>
</tr>

<tr>
<td>nome</td>
<td>Nome da disciplina</td>
<td>VARCHAR(100)</td>
<td>Não aceita valor nulo</td>
</tr>

<tr>
<td>carga_horaria</td>
<td>Carga horária da disciplina</td>
<td>INT</td>
<td>Não aceita valor nulo</td>
</tr>
</table>

---

## 🚪 Entidade Sala

<table>
<tr>
<th>Atributo</th>
<th>Descrição</th>
<th>Domínio</th>
<th>Restrição do atributo</th>
</tr>

<tr>
<td>id_sala</td>
<td>Identificador da sala</td>
<td>INT</td>
<td>Chave Primária (PK)</td>
</tr>

<tr>
<td>numero_sala</td>
<td>Número da sala</td>
<td>VARCHAR(10)</td>
<td>Não aceita valor nulo</td>
</tr>

<tr>
<td>capacidade</td>
<td>Capacidade da sala</td>
<td>INT</td>
<td>Não aceita valor nulo</td>
</tr>

<tr>
<td>bloco</td>
<td>Bloco da sala</td>
<td>VARCHAR(20)</td>
<td>Não aceita valor nulo</td>
</tr>
</table>

---

## 💰 Entidade Pagamento

<table>
<tr>
<th>Atributo</th>
<th>Descrição</th>
<th>Domínio</th>
<th>Restrição do atributo</th>
</tr>

<tr>
<td>id_pagamento</td>
<td>Identificador do pagamento</td>
<td>INT</td>
<td>Chave Primária (PK)</td>
</tr>

<tr>
<td>valor</td>
<td>Valor do pagamento</td>
<td>DECIMAL(10,2)</td>
<td>Não aceita valor nulo</td>
</tr>

<tr>
<td>data_pagamento</td>
<td>Data do pagamento</td>
<td>DATE</td>
<td>Não aceita valor nulo</td>
</tr>

<tr>
<td>forma_pagamento</td>
<td>Forma de pagamento</td>
<td>VARCHAR(30)</td>
<td>Não aceita valor nulo</td>
</tr>
</table>

---

## 📅 Entidade Frequencia

<table>
<tr>
<th>Atributo</th>
<th>Descrição</th>
<th>Domínio</th>
<th>Restrição do atributo</th>
</tr>

<tr>
<td>id_frequencia</td>
<td>Identificador da frequência</td>
<td>INT</td>
<td>Chave Primária (PK)</td>
</tr>

<tr>
<td>data_aula</td>
<td>Data da aula</td>
<td>DATE</td>
<td>Não aceita valor nulo</td>
</tr>

<tr>
<td>presenca</td>
<td>Presença do aluno</td>
<td>BOOLEAN</td>
<td>Não aceita valor nulo</td>
</tr>
</table>

---

## 📄 Entidade Certificado

<table>
<tr>
<th>Atributo</th>
<th>Descrição</th>
<th>Domínio</th>
<th>Restrição do atributo</th>
</tr>

<tr>
<td>id_certificado</td>
<td>Identificador do certificado</td>
<td>INT</td>
<td>Chave Primária (PK)</td>
</tr>

<tr>
<td>data_emissao</td>
<td>Data de emissão</td>
<td>DATE</td>
<td>Não aceita valor nulo</td>
</tr>

<tr>
<td>codigo_validacao</td>
<td>Código de validação</td>
<td>VARCHAR(50)</td>
<td>Único e não nulo</td>
</tr>
</table>