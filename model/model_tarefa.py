from database.conexao import conectar_bd

def inserir_tarefa(texto_tarefa):
    conexao, cursor = conectar_bd()

    cursor.execute("""
                                INSERT INTO tarefas (tarefa, status)
                                VALUES (?, ?);
                                """,
                                [texto_tarefa, "Pendente"])

    conexao.commit()
    conexao.close()

def recuperar_tarefas():
    conexao, cursor = conectar_bd()

    cursor.execute("""
                        SELECT cod_tarefa, status, tarefa FROM tarefas;""")

    tarefas = cursor.fetchall() #commit
    conexao.close()

    return tarefas
