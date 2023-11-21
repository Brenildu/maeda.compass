# Busca por valores
# Permite a busca por valores máximos e mínimos dentro do array.
# argmax: retorna o índice do maior valor
# argmin: retorna o índice do menor valor
# max: retorna o maior valor
# min: retorno o menor valor
import numpy as np

a = np.random.choice(30,size=10, replace=False)
print("A: ",a)
print("Maior valor",np.max(a))
print("Menor valor",np.min(a))
print("Índice do maior valor",np.argmax(a))
print("Índice do menor valor",np.argmin(a))

