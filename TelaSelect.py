import PySimpleGUI as sg
import Banco
import main
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
            [sg.Button('Voltar')],
            [sg.Output(size = (45,30))]
        ]
        #janela 

        self.janela = sg.Window('Dados do Produto').layout(layout)
    
    def Iniciar(self):      
        while True:
            #Extrair os dados da tela
            event, self.values = self.janela.Read()
            if event == 'Visualizar produtos cadastrados produtos': 
                #Recebe os valores do Formulário
                id = self.values['id']
                if id == '':
                    print('-'*20)
                    Banco.select()
                else:
                    print('-'*20)
                    Banco.selectid(id)
            if event == 'Voltar':
                self.janela.close()
                tela = main.TelaInicio()
                tela.Iniciar()  
                
            if event == sg.WIN_CLOSED:
                break
                
