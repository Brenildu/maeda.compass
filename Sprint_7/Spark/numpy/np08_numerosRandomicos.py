#NumPy oferece uma biblioteca, numpy.random, para geração de números randômicos. Os principais métodos são: random
# Gera amostra valores no intervalo [0, 1)
# Aceita como parâmetro o número de dimensões do array
import numpy as np

a = np.random.random(4)
b = np.random.random((5,3))
print("A:", a)
print("B:", b)

print("\n==================\n")

# randint
# Gera amostra de valores inteiros
# Aceita como parâmetros:
# limite inferior
# limite superior
# dimensões do array

a = np.random.randint(5)
print(a)

a = np.random.randint(6,10)
print(a)

a = np.random.randint(low=6,high=10,size=3)
print(a)

a = np.random.randint(low=6,high=10,size=(2,2))
print(a)

print("\n==================\n")
# choice
# Gera amostra valores a partir de uma distribuição de probabilidades
# Aceita como parâmetros:
# a - Valores
# size - Número de amostras
# replace - Se a amostragem é com reposição
# p - Distribuição de probabilidades

caracteres=['a','b','c','d','e','f']
a = np.random.choice(caracteres)
print(a)

caracteres=['a','b','c','d','e','f']
a = np.random.choice(caracteres,size=10)
print(a)

caracteres=['a','b','c','d','e','f']
a = np.random.choice(caracteres,size=3,replace=False)
print(a)

caracteres=['a','b','c','d','e','f']
probabilidades = [0.2,.1,.3,.1,.2,.1]
a = np.random.choice(caracteres,size=100,p=probabilidades)
from collections import Counter
for caractere, contagem in Counter(a).items():
 print("{} - Ocorrências: {} - Frequência: {}".format(caractere,
contagem,contagem/100))
 
print("\n==================\n")
