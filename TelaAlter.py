import PySimpleGUI as sg
import Banco
import main
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
            [sg.Button('Retirar produtos do estoque')],
            [sg.Button('Voltar')],
            [sg.Output(size = (35,20))]
        ]
        #janela 

        self.janela = sg.Window('Dados do Produto').layout(layout)
    
    def Iniciar(self):      
        while True:
            #Extrair os dados da tela
            event, self.values = self.janela.Read()
            #Recebe os valores do Formulário
            id = self.values['id']
            quantidade = self.values['quantidade']

            if event == 'Retirar produtos do estoque':
                    #Recebe os valores do Formulário
                    id = self.values['id']
                    quantidade = self.values['quantidade']
                    print('Foram retiradas ' + quantidade + ' unidades ao produto de id: ' + id)
                    Banco.alter(id,quantidade)
                #Volta ao formulário inicial
            if event == 'Voltar':
                self.janela.close()
                tela = main.TelaInicio()
                tela.Iniciar()  
                
            if event == sg.WIN_CLOSED:
                break