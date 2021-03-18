import PySimpleGUI as sg
import Banco

#TELA PARA CONSULTA DE PRODUTOS CADASTRADOS
class TelaPython:
    def __init__(self):
        #MEXER NOS ESTILOS
        sg.change_look_and_feel('DarkBlue11')
        #layout
        layout = [
            #[sg.Text('Busque pelo ID, não preencha o ID e veja todos', size = (40,0))]
            [sg.Text('ID', size = (5,0)),sg.Input(size = (10,0), key ='id')],
            [sg.Button('Visualizar produtos cadastrados produtos')],
            [sg.Output(size = (45,20))]
        ]
        #janela 

        self.janela = sg.Window('Dados do Produto').layout(layout)
    
    def Iniciar(self):      
        while True:
            #Extrair os dados da tela
            self.button, self.values = self.janela.Read()
            #Recebe os valores do Formulário
            id = self.values['id']
            if id == '':
                print('-'*20)
                Banco.select()
            else:
                print('-'*20)
                Banco.selectid(id)
