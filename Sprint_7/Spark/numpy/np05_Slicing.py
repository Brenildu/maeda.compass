# Aplicando Slicing
# Assim como em listas de Python, NumPy arrays também podem ser fatiados (slicing)
# Slicing é a técnica de “fatiar” um contêiner que suporta indexação linear
# O fatiamento se dá adicionando um par de colchetes ao fim da variável
# Possui 3 parâmetros: início (incluso), fim (excluso) e passo
# Em nosso primeiro exemplo, estamos utilizando um array unidimensional (vetor), aplicando sobre ele operações de fatiamento.

import numpy as np

array = np.arange(20)
print("Array completo - ", array)
print("A partir do indice 2 (incluso) - ", array[2:])
print("Ate o índice 2 (excluso) - ", array[:2])
print("Do indice 4 até 8 (excluso) - ", array[4:8])
print("Desconsiderar os 2 ultimos - ", array[:-2])
print("Considerar apenas os 2 ultimos - ", array[-2:])

array[18:20] = [-1,-2]
print("Array modificado após atribuição - ", array)


print("\n==================\n")

matrix = np.arange(10).reshape((2,5))

print("Array completo - \n", matrix)
print("Primeira linha - ", matrix[0,:])
print("Primeira coluna - ", matrix[:,0])
print("Ultima linha - ", matrix[-1,:])
print("Ultima coluna - ", matrix[:,-1])
print("Colunas 2 e 3 - \n", matrix[ :,2:4])

print("\n==================\n")

