#!C:\Users\breno\AppData\Local\Programs\Python\Python311\python.exe
class Humano:
    # Atributo de classe, o mesmo valor para todas as instancias
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome
        self._idade = None

    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, idade):
        if idade < 0:
            raise ValueError('Idade deve ser um numero positivo')
        self._idade = idade

    def das_cavernas(self):
        # esse atributo vai prevalecer com o atributo da classe
        self.especie = 'Homo Neanderthalensis'
        return self

    # um metodo que poderia estar fora da classe que teria a mesma função
    # é importante estar na classe para facilitar a associação do uso
    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Neanderthalensis', 'Sapiens ')
        return ('Australopiteco',) + tuple(f'Homo {adj}' for adj in adjetivos)
    
    # é possivel diferenciar a classe a partir da comparação
    # pode chama-lo de multiplas formas diferentes
    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]


class Neanderthal(Humano):
    especie = Humano.especies()[-2]


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]


if __name__ == '__main__':
    jose = HomoSapiens('Jose')
    # acessa como se fosse um atributo
    jose.idade = 40
    print(f'Nome: {jose.nome} idade: {jose.idade}')