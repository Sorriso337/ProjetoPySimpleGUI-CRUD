import PySimpleGUI as sg
import TelaInsert 
import TelaSelect
import TelaAlterPlus
import TelaAlter

class TelaInicio:
    def __init__(self):
        #MEXER NOS ESTILOS
        sg.change_look_and_feel('DarkBlue11')
        #layout
        layout1 = [
            [sg.Text('Para qual área seguir?')],
            [sg.Button('Cadastro', size = (10,1))],
            [sg.Button('Consulta',size = (10,1))],
            [sg.Button('Adicionar',size = (10,1))],
            [sg.Button('Retirada',size = (10,1))],
        ]
        #janela 

        self.janela = sg.Window('Início', icon = 'img/logo.png').layout(layout1)
    
    def Iniciar(self):      
        while True:
            event, values = self.janela.read()

            if event == sg.WIN_CLOSED:
                break   
            
            if event == 'Cadastro':
                self.janela.close( )
                tela = TelaInsert.TelaPython()
                tela.Iniciar()
            if event == 'Consulta':
                self.janela.close()
                tela = TelaSelect.TelaPython()
                tela.Iniciar()
            if event == 'Adicionar':
                self.janela.close()
                tela = TelaAlterPlus.TelaPython()
                tela.Iniciar()
            if event == 'Retirada':
                self.janela.close()
                tela = TelaAlter.TelaPython()
                tela.Iniciar()
            

            #Extrair os dados da tela
            self.button, self.values = self.janela.Read()