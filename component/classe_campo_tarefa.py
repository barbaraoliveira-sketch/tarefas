import flet as ft

class Campo_tarefa(ft.Row):
    def __init__(self, texto_tarefa, funcao_excluir, cod_tarefa):
        super().__init__()

        self.cod_tarefa = cod_tarefa

        self.funcao_excluir = funcao_excluir

        self.caixa_texto = ft.TextField(value = texto_tarefa,
                                    filled=True,
                                   bgcolor="#C546D1",
                                   read_only= True,
                                   border_color= "#C546D1",
                                   border_radius= 30)

        self.caixa_selecao = ft.Checkbox(on_change= self.alterar_cor)

        self.caixa_bonita = ft.Container(content=ft.Row(controls=[self.caixa_selecao,
                                                             self.caixa_texto,]
                                                             ),

                                                             bgcolor="#B300C4",
                                                             border=ft.Border.all(width=1,
                                                                                  color="#ffc1fc"),

                                                            border_radius=10,
                                                            padding=20,
                                                            )

        self.botao_excluir = ft.Button(content = "excluir",
                                bgcolor= "#ad0000",
                                color="#ffffff",
                                on_click = lambda: self.funcao_excluir(self))

        self.botao_editar = ft.Button(
            content = "editar",
                                bgcolor="#4389f3",
                                color="#ffffff"
                                )

        self.estado = ft.Text(value = "concluido")

        self.coluna = ft.Column(controls = [self.estado,
                                            self.caixa_bonita])

        self.linha_botoes = ft.Column(controls=[self.botao_excluir, self.botao_editar])

        self.controls = [self.coluna, self.linha_botoes]


    def alterar_cor(self):
        if self.caixa_selecao.value == True:
            self.caixa_bonita.bgcolor = "#e02727"
            self.estado.value
        
            
        else:
            self.caixa_bonita.bgcolor = "#B300C4"
            self.estado.value = "Pendente"

    @property
    def value(self):
        return self.caixa_texto.value