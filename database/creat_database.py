from database.conexao import conectar_bd

def criar_banco_dados():

    #Criando a tabels de tarefas no banco de dados sqlite3
        conexao, cursor = conectar_bd()
        cursor.execute("""
                            CREATE TABLE if NOT EXISTS tarefas (
                            cod_tarefa INTEGER PRIMARY KEY AUTOINCREMENT,
                            tarefa TEXT,
                            status TEXT);
                            """)
        conexao.commit() # Salvando alterações 
        conexao.close() # Fechando conexão
    