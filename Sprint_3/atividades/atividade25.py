class Avião:
    cor = "Azul"  # Atributo de classe para a cor fixa

    def __init__(self, modelo, velocidade_maxima, capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.capacidade = capacidade

# Entradas
entradas = [
    ("BOIENG456", "1500 km/h", 400),
    ("Embraer Praetor 600", "863 km/h", 14),
    ("Antonov An-2", "258 km/h", 12)
]

# Instanciando objetos da classe Avião
aviões = []
for entrada in entradas:
    modelo, velocidade, capacidade = entrada
    avião = Avião(modelo, velocidade, capacidade)
    aviões.append(avião)

# Imprimindo informações dos aviões
for avião in aviões:
    print(f"O avião de modelo {avião.modelo} possui uma velocidade máxima de {avião.velocidade_maxima}, capacidade para {avião.capacidade} passageiros e é da cor {Avião.cor}.")