# 📘 Modelo Lógico

---

## 👤 Aluno

Aluno (
 id_aluno PK,
 nome,
 cpf,
 email,
 telefone,
 data_nascimento
)

---

## 📘 Curso

Curso (
 id_curso PK,
 nome,
 carga_horaria,
 duracao_meses,
 valor
)

---

## 👨‍🏫 Professor

Professor (
 id_professor PK,
 nome,
 especialidade,
 email,
 telefone
)

---

## 🚪 Sala

Sala (
 id_sala PK,
 numero_sala,
 capacidade,
 bloco
)

---

## 📚 Disciplina

Disciplina (
 id_disciplina PK,
 nome,
 carga_horaria,
 id_curso FK
)

---

## 🏫 Turma

Turma (
 id_turma PK,
 nome_turma,
 turno,
 semestre,
 id_curso FK,
 id_professor FK,
 id_sala FK
)

---

## 📝 Matricula

Matricula (
 id_matricula PK,
 data_matricula,
 status,
 id_aluno FK,
 id_turma FK
)

---

## 💰 Pagamento

Pagamento (
 id_pagamento PK,
 valor,
 data_pagamento,
 forma_pagamento,
 id_matricula FK
)

---

## 📅 Frequencia

Frequencia (
 id_frequencia PK,
 data_aula,
 presenca,
 id_matricula FK
)

---

## 📄 Certificado

Certificado (
 id_certificado PK,
 data_emissao,
 codigo_validacao,
 id_matricula FK
)

---

# 🔑 Chaves Primárias (PK)

| Tabela | Chave Primária |
|---|---|
| Aluno | id_aluno |
| Curso | id_curso |
| Professor | id_professor |
| Sala | id_sala |
| Disciplina | id_disciplina |
| Turma | id_turma |
| Matricula | id_matricula |
| Pagamento | id_pagamento |
| Frequencia | id_frequencia |
| Certificado | id_certificado |

---

# 🔗 Chaves Estrangeiras (FK)

| Tabela | Chave Estrangeira | Referência |
|---|---|---|
| Disciplina | id_curso | Curso(id_curso) |
| Turma | id_curso | Curso(id_curso) |
| Turma | id_professor | Professor(id_professor) |
| Turma | id_sala | Sala(id_sala) |
| Matricula | id_aluno | Aluno(id_aluno) |
| Matricula | id_turma | Turma(id_turma) |
| Pagamento | id_matricula | Matricula(id_matricula) |
| Frequencia | id_matricula | Matricula(id_matricula) |
| Certificado | id_matricula | Matricula(id_matricula) |

---

# 📘 Normalização do Banco de Dados

## ✅ 1FN (Primeira Forma Normal)

Todos os atributos são atômicos, ou seja, não possuem valores múltiplos ou listas dentro de um único campo.

### Exemplo:
O atributo `telefone` armazena apenas um valor por registro, e não uma lista de telefones.

---

## ✅ 2FN (Segunda Forma Normal)

O banco está na 1FN e todos os atributos não-chave dependem totalmente da chave primária da tabela, não existindo dependência parcial.

### Exemplo:
Na entidade `Matricula`, o atributo `status` depende da matrícula como um todo, e não apenas do aluno ou apenas da turma.

---

## ✅ 3FN (Terceira Forma Normal)

O banco está na 2FN e não possui dependências transitivas, ou seja, atributos não-chave não dependem de outros atributos não-chave.

### Exemplo:
O atributo `nome` do aluno depende diretamente do `id_aluno`, e não de outro atributo da tabela.

---

# 💾 Estrutura SQL

```sql
CREATE DATABASE IF NOT EXISTS instituicao_cursos;

USE instituicao_cursos;

CREATE TABLE Aluno(
    id_aluno INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(14) UNIQUE NOT NULL,
    email VARCHAR(100) NOT NULL,
    telefone VARCHAR(15),
    data_nascimento DATE
);

CREATE TABLE Curso(
    id_curso INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    carga_horaria INT,
    duracao_meses INT,
    valor DECIMAL(10,2)
);

CREATE TABLE Professor(
    id_professor INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    especialidade VARCHAR(100),
    email VARCHAR(100),
    telefone VARCHAR(15)
);

CREATE TABLE Sala(
    id_sala INT AUTO_INCREMENT PRIMARY KEY,
    numero_sala VARCHAR(10),
    capacidade INT,
    bloco VARCHAR(20)
);

CREATE TABLE Disciplina(
    id_disciplina INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    carga_horaria INT,
    id_curso INT,
    FOREIGN KEY (id_curso) REFERENCES Curso(id_curso)
    ON DELETE SET NULL
    ON UPDATE CASCADE
);

CREATE TABLE Turma(
    id_turma INT AUTO_INCREMENT PRIMARY KEY,
    nome_turma VARCHAR(50),
    turno VARCHAR(20),
    semestre VARCHAR(20),
    id_curso INT,
    id_professor INT,
    id_sala INT,
    FOREIGN KEY (id_curso) REFERENCES Curso(id_curso)
    ON DELETE SET NULL
    ON UPDATE CASCADE,
    
    FOREIGN KEY (id_professor) REFERENCES Professor(id_professor)
    ON DELETE SET NULL
    ON UPDATE CASCADE,
    
    FOREIGN KEY (id_sala) REFERENCES Sala(id_sala)
    ON DELETE SET NULL
    ON UPDATE CASCADE
);

CREATE TABLE Matricula(
    id_matricula INT AUTO_INCREMENT PRIMARY KEY,
    data_matricula DATE,
    status VARCHAR(20),
    id_aluno INT,
    id_turma INT,
    
    FOREIGN KEY (id_aluno) REFERENCES Aluno(id_aluno)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    
    FOREIGN KEY (id_turma) REFERENCES Turma(id_turma)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

CREATE TABLE Pagamento(
    id_pagamento INT AUTO_INCREMENT PRIMARY KEY,
    valor DECIMAL(10,2),
    data_pagamento DATE,
    forma_pagamento VARCHAR(30),
    id_matricula INT,
    
    FOREIGN KEY (id_matricula) REFERENCES Matricula(id_matricula)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

CREATE TABLE Frequencia(
    id_frequencia INT AUTO_INCREMENT PRIMARY KEY,
    data_aula DATE,
    presenca BOOLEAN,
    id_matricula INT,
    
    FOREIGN KEY (id_matricula) REFERENCES Matricula(id_matricula)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

CREATE TABLE Certificado(
    id_certificado INT AUTO_INCREMENT PRIMARY KEY,
    data_emissao DATE,
    codigo_validacao VARCHAR(50) UNIQUE,
    id_matricula INT UNIQUE,
    
    FOREIGN KEY (id_matricula) REFERENCES Matricula(id_matricula)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);