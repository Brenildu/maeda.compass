#!C:\Users\breno\AppData\Local\Programs\Python\Python311\python.exe
class Humano:
    # Atributo de classe, o mesmo valor para todas as instancias
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        # esse atributo vai prevalecer com o atributo da classe
        self.especie = 'Homo Neanderthalensis'
        return self


if __name__ == '__main__':
    jose = Humano('José')
    grokn = Humano('grokn').das_cavernas()

    print(f'Humano.especie: {Humano.especie}')
    print(f'jose.especie: {jose.especie}')
    print(f'grokn.especie: {grokn.especie}')