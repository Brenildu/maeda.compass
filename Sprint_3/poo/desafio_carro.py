class Carro():
    def __init__(self, velocidade_max):
        self.velocidade_max = velocidade_max
        self.velocidade_atual = 0

    def acelerar(self, delta=5):
        maxima = self.velocidade_max
        velo_atual = self.velocidade_atual + delta 
        self.velocidade_atual = velo_atual if velo_atual <= maxima else maxima
        return self.velocidade_atual

    def frear(self, delta):
        velo_atual = self.velocidade_atual - delta 
        self.velocidade_atual = velo_atual if velo_atual >= 0 else 0
        return self.velocidade_atual
    

if __name__ == '__main__':
    c1 = Carro(180)

    for _ in range(25):
        print(c1.acelerar(8))

    for _ in range(10):
        print(c1.frear(delta=20))