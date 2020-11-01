import random

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
        input('Faça sua pergunta: ')
        print(random.choice(self.answers))

myAnswer = pyDecide()
myAnswer.start()