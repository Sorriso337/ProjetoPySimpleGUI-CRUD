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
            [sg.Button('Cadastro'),sg.Button('Consulta')],
            [sg.Button('Adicionar'),sg.Button('Retirada')],
        ]
        #janela 

        self.janela = sg.Window('Início', icon = 'img/inicio.png').layout(layout1)
    
    def Iniciar(self):      
        while True:
            event, values = self.janela.read()
            if event == sg.WIN_CLOSED:
                break
            
            if event == 'Cadastro':
                tela = TelaInsert.TelaPython()
                tela.Iniciar()
                self.janela.Hide()
            if event == 'Consulta':
                tela = TelaSelect.TelaPython()
                tela.Iniciar()
                self.janela.Hide()
            if event == 'Adicionar':
                tela = TelaAlterPlus.TelaPython()
                tela.Iniciar()
                self.janela.Hide()
            if event == 'Retirada':
                tela = TelaAlter.TelaPython()
                tela.Iniciar()
                self.janela.Hide()
            

            #Extrair os dados da tela
            self.button, self.values = self.janela.Read()
            #Recebe os valores do Formulário
            

tela = TelaInicio()
tela.Iniciar()
