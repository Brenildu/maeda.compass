# Implemente duas classes, Pato e Pardal , que herdam de uma superclasse chamada Passaro as habilidades de voar e emitir som.

# Contudo, tanto Pato quanto Pardal devem emitir sons diferentes (de maneira escrita) no console, conforme o modelo a seguir.

# Imprima no console exatamente assim:

# Pato
# Voando...
# Pato emitindo som...
# Quack Quack
# Pardal
# Voando...
# Pardal emitindo som...
# Piu Piu

class Passaro():

    def __init__(self, som):
        self.som = som

    def voar(self):
        print(f'Voando...')

    def emitir_som(self):
        print(f'{self.som}')


class Pato(Passaro):
    pass


class Pardal(Passaro):
    pass


if __name__ == '__main__':
    
    pato = Pato('Quack Quack')
    pardal = Pardal('Piu Piu')

    print('Pato')
    pato.voar()
    pato.emitir_som()

    print('Pardal')
    pardal.voar()
    pardal.emitir_som()