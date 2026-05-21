from dotenv import load_dotenv
import os
import mysql.connector

# Carrega as variáveis do arquivo .env
load_dotenv(dotenv_path='.env')

senha = os.getenv("SENHA")

try:
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password=senha,
        database='instituicao_cursos'
    )
    cursor = conn.cursor()

    sql = "SELECT \
	T.nome_turma AS Turma, \
	COUNT(M.id_matricula) AS QtdAlunos \
FROM\
	Turma AS T \
LEFT JOIN Matricula AS M ON \
	T.id_turma = M.id_turma \
GROUP BY \
	T.nome_turma;"
    print('\nQuantidade de Alunos por Turma: ')
    cursor.execute(sql)
    for row in cursor.fetchall():
        print(row)
    print("====================================")
    print("Cursos e Disciplinas: ")

    sql = "SELECT Curso.nome as Curso_nome, Disciplina.nome as Disciplina_nome FROM Curso INNER JOIN Disciplina ON Disciplina.id_curso = Curso.id_curso order by (Curso_nome);"
    cursor.execute(sql)
    for row in cursor.fetchall():
        print(row)
    # Verifica a presença por Turma e data
    print("\nPesquisar Presenças por dia")

    sql = "SELECT t.nome_turma, f.data_aula, a.nome AS nome_aluno, CASE WHEN f.presenca = 1 THEN 'Presente' ELSE 'Ausente' END AS status_presenca FROM Frequencia as f INNER JOIN Matricula m ON f.id_matricula = m.id_matricula INNER JOIN Aluno a ON m.id_aluno = a.id_aluno INNER JOIN Turma t ON m.id_turma = t.id_turma WHERE t.id_turma = %s  AND f.data_aula = %s  ORDER BY a.nome;"

    turmaId = int(input("Escolha a sua turma: "))
    dataAula = str(input("Diga uma data(YYYY-MM-DD): "))
    if turmaId == '' or dataAula == '':
        raise ValueError("Digite valores válidos para turma e data.")
    cursor.execute(sql, (turmaId, dataAula))
    for row in cursor.fetchall():
        print(row)


except mysql.connector.Error as err:
    print('Erro de conexão:', err)
finally:
    try:
        cursor.close()
    except NameError:
        pass
    try:
        conn.close()
    except NameError:
        pass