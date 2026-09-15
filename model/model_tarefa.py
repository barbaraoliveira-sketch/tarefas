from database.conexao import conectar_bd

def inserir_tarefa(texto_tarefa):
    
    conexao, cursor = conectar_bd()
    cursor.execute("""
                                INSERT INTO tarefas (tarefa, status)
                                VALUES (?, ?);
                                """,
                                [texto_tarefa, "Pendente"])
    conexao.commit()
    cod_tarefa = cursor.lastrowid
    conexao.close()
    return cod_tarefa

def recuperar_tarefas():
    conexao, cursor = conectar_bd()
    cursor.execute("""
                        SELECT cod_tarefa, status, tarefa FROM tarefas;""")

    tarefas = cursor.fetchall() #commit
    conexao.close()

    return tarefas

def deletar_tarefa(codigo_tarefa):
    conexao, cursor = conectar_bd()
    cursor.execute("""
                    DELETE FROM tarefas
                    WHERE cod_tarefa = ?;
                    """,
                    [codigo_tarefa])
    conexao.commit()
    conexao.close()