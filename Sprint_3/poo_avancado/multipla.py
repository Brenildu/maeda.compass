#!C:\Users\breno\AppData\Local\Programs\Python\Python311\python.exe
class Animal:
    @property
    def capacidade(self):
        return ('dormir', 'comer', 'beber')


class Homem(Animal):
    @property
    def capacidade(self):
        return super().capacidade + ('amar', 'falar', 'estudar')
    

class Aranha(Animal):
    @property
    def capacidade(self):
        return super().capacidade + ('fazer teia', 'andar pelas paredes')
    

class SpiderMan(Homem, Aranha):
    @property
    def capacidade(self):
        return super().capacidade + ('bater em bandidos', 'atirar teias em predios')
    

if __name__ == '__main__':
    john = Homem()
    print(f'John: {john.capacidade}')

    aranha = Aranha()
    print(f'aranha: {aranha.capacidade}')

    peter = SpiderMan()
    print(f'Peter Parker: {peter.capacidade}')