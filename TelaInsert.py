import PySimpleGUI as sg
import Banco

#TELA PARA INSERÇÃO DE PRODUTOS NO ESTOQUE
class TelaPython:
    def __init__(self):
        #MEXER NOS ESTILOS
        sg.change_look_and_feel('DarkBlue11')
        #layout
        layout = [
            [sg.Text('Nome', size = (5,0)),sg.Input(size = (10,0), key ='nome')],
            [sg.Text('Preco', size = (5,0)),sg.Input(size = (10,0), key = 'preco')],
            [sg.Text('Quantidade', size = (5,0)), sg.Input(size = (10,0), key ='quantidade')],
            [sg.Button('Cadastrar produtos')],
            #[sg.Button('Voltar')],
            [sg.Output(size = (35,20))]
        ]
        #janela 

        self.janela = sg.Window('Dados do Produto').layout(layout)
    
    def Iniciar(self):      
        while True:
            #Extrair os dados da tela
            self.button, self.values = self.janela.Read()
            #Recebe os valores do Formulário
            #if self.event == 'Cadastrar produtos':
            nome = self.values['nome']
            preco = self.values['preco']
            quantidade = self.values['quantidade']
            disponibilidade = 0
            if quantidade == '':
                quantidade = 0
            if int(quantidade) > 0:
                disponibilidade = 1   
            #Retorna no Outpot os valores
            print(f'Nome: {nome}')
            print(f'preco: {preco}')
            print(f'Quantidade: {quantidade}')
            print(f'Disponibilidade: {disponibilidade}')


                #Insert no banco chamando a função insert do arquivo Banco.py
            Banco.insert(self,nome,preco,quantidade,disponibilidade)

            #Volta ao formulário inicial
            #if event == 'Voltar':
            #   tela = main.TelaInicio()
            #    tela.Iniciar()  
            
            #if event == sg.WIN_CLOSED:
                #break
            
