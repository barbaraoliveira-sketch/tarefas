import flet as ft

class Campo_tarefa(ft.Row):
    def __init__(self, texto_tarefa):
        super().__init__()

        self.caixa_texto = ft.TextField(value = texto_tarefa,
                                    filled=True,
                                   bgcolor="#C546D1",
                                   read_only= True,
                                   border_color= "#C546D1",
                                   border_radius= 30)

        self.caixa_selecao = ft.Checkbox(on_change= self.alterar_cor)

        self.caixa_bonita = ft.Container(content=ft.Row(controls=[self.caixa_selecao,
                                                             self.caixa_texto,
                                                             ft.Button("excluir",
                                                                       bgcolor= "#ad0000",
                                                                       color="#ffffff"),


                                                             ft.Button("editar",
                                                                       bgcolor="#4389f3",
                                                                       color="#ffffff"),

                                                            ft.Text(value = "Concluido",),
                                                            ft.Text(value = "Pendente")]
                                                             ),
                                                             bgcolor="#B300C4",
                                                             border=ft.Border.all(width=1,
                                                                                  color="#ffc1fc"),
                                                            border_radius=10,
                                                            padding=20,
                                                            )

        self.botao_excluir = ft.Button

        self.controls = [self.caixa_bonita]

    def alterar_cor(self):
        if self.caixa_selecao.value == True:
            self.caixa_bonita.bgcolor = "#e02727"
            self.caixa_bonita.value == "Concluido"
        else:
            self.caixa_bonita.bgcolor = "#B300C4"
            self.caixa_bonita.value == "Pendente"

    @property
    def value(self):
        return self.caixa_texto.value