import PySimpleGUI as sg
import Banco

#TELA PARA RETIRADA DE PRODUTOS DO ESTOQUE
class TelaPython:
    def __init__(self):
        #MEXER NOS ESTILOS
        sg.change_look_and_feel('DarkBlue11')
        #layout
        layout = [
            #[sg.Text('Busque pelo ID, não preencha o ID e veja todos', size = (40,0))]
            [sg.Text('ID', size = (10,0)),sg.Input(size = (10,0), key ='id')],
            [sg.Text('Quantidade', size = (10,0)),sg.Input(size = (10,0), key ='quantidade')],
            [sg.Button('Retirar produtos do estoque')]
        ]
        #janela 

        self.janela = sg.Window('Dados do Produto').layout(layout)
    
    def Iniciar(self):      
        while True:
            #Extrair os dados da tela
            self.button, self.values = self.janela.Read()
            #Recebe os valores do Formulário
            id = self.values['id']
            quantidade = self.values['quantidade']

            Banco.alter(id,quantidade)
            