MAIOR_IDADE = 18


class Pessoa():

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        if not self.idade:
            return self.nome
        return f'{self.nome}: {self.idade} anos'
        
    def isAdult(self):
        adulto = 'Sim' if self.idade > 18 else 'Não'
        return f'{self.nome}, {adulto} é um adulto'