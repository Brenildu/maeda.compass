from .pessoa import Pessoa


class Vendedor(Pessoa):
    def __init__(self, nome, idade, salario=0):
        super().__init__(nome, idade)
        self.salario = salario  