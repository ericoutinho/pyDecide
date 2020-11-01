import random
import PySimpleGUI as sg

class pyDecide:
    def __init__(self):
        self.answers = [
            'Sim',
            'Não',
            'Você quem sabe',
            'Escolha como fica melhor para você',
            'Boa!',
            'Já era hora',
            'Sai fora'
        ]
    def start(self):

        layout = [
            [sg.Text('Faça a sua pergunta:', size=(45,0))],
            [sg.InputText(size=(45,0), key="pergunta")],
            [sg.Button('Obter resposta', key="responder"), sg.Button('Cancelar', key="cancelar")],
            [sg.Output(size=(40,10))]
        ]
        window = sg.Window('PyDecideGUI', layout=layout)
        while True:
            event, value = window.Read()
            if event == sg.WINDOW_CLOSED:
                break
            if event == 'cancelar':
                window.close()
            if event == 'responder':
                if len(value['pergunta']) > 4 :
                    print(random.choice(self.answers))
                    window.find('pergunta').update('')
                else:
                    print('É necessário fazer uma pergunta!')
                    window.find('pergunta').update('')

myAnswer = pyDecide()
myAnswer.start()