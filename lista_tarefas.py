import flet as ft
from component.classe_campo_tarefa import Campo_tarefa
import sqlite3

def main(pagina:ft.Page):
    pagina.title = "Checklist"
    pagina.bgcolor = "#D094DF"
    pagina.horizontal_alignment = "center"

    #Criando a tabels de tarefas no banco de dados sqlite3
    conexao = sqlite3.connect("bd_tarefas.sqlite") #Conectando banco de dados
    cursor = conexao.cursor() #Criando cursor
    cursor.execute("""
                        CREATE TABLE if NOT EXISTS tarefas (
                        cod_tarefa INTEGER PRIMARY KEY AUTOINCREMENT,
                        tarefa TEXT
                        status TEXT);
                        """)
    conexao.commit() # Salvando alterações 
    conexao.close() # Fechando conexão

    titulo = ft.Text(value="Checklist - Tudo em Dia",
                     size = 40,
                     font_family = "Broadway",
                     color= "#D31DE4")

    sub_titulo = ft.Text(value="Digite no campo abaixo a tarefa que deseja incluir",
                         size = 20,
                         font_family = "Broadway",
                         color= "#D31DE4")

    lista_tarefas = []
    

    def excluir_campo(campo_tarefa):
            lista_tarefas.remove(campo_tarefa)

    def adicionar_tarefa():
        novo_campo = Campo_tarefa(texto_tarefa = campo_incluir.value,
                                  funcao_excluir= excluir_campo)
        lista_tarefas.append(novo_campo)
        campo_incluir.value = ""

    

    campo_incluir = ft.TextField(label = "Digite aqui:",
                               bgcolor = "#B300C4",
                               border_radius = 30,
                               border_color= "#B300C4",
                               border_width= 3,
                                width= 400,
                                height= 45,
                                )

    botao_incluir = ft.Button(content = "incluir",
                      width= 100,
                      height= 45,
                        color= "#ffffff",
                        bgcolor= "#FF9AD8",
                        on_click=adicionar_tarefa)

    
    

    tarefas = ft.Column(controls=lista_tarefas,
                             #expand=True,
                             #wrap=True,
                             scroll=ft.ScrollMode.AUTO)
                             #horizontal_alignment="center")

    tarefas1 = ft.Row(controls = tarefas,alignment=ft.MainAxisAlignment.CENTER)


    linha = ft.Row(controls=[campo_incluir,
                             botao_incluir,],
                             alignment="center",
                             spacing=30)


    pagina.controls = [titulo,
                        sub_titulo,
                       linha,
                       tarefas1,
                       
                                      
                       ]

    pagina.update()
ft.run(main)