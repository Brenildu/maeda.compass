#Series
# Representa um conjunto de dados unidimensionais (array, atributo)
# Pode ser resultado de uma seleção sobre um DataFrame ou poder ser criada diretamente
import pandas as pd

serie = pd.Series (['Amarelo', 'Verde', 'Azul'])
print(serie)
print("Valor para o indice 0 1 2", serie[0], serie[1], serie[2])

serie_2 = pd.Series( dict(amarelo=10, verde=3, pedro=60))
print(serie_2)
print("Valor para o indice 'amarelo'", serie_2['amarelo'], serie_2[0])
print(":Indices da serie", serie_2.index)