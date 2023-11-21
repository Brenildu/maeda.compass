# Operações com arrays
# Algumas operações com arrays incluem:
# divisão, multiplicação, soma, subtração
# junção
# transposição
# atribuição
# operações binárias e lógicas
# Algumas operações com arrays incluem:
# divisão, multiplicação, soma, subtração

import numpy as np

a = np.arange(0,5,dtype=np.int32)
b = np.arange(6,11,dtype=np.int32)

print("A:",a)
print("B:",b)
print ("A + B:",a+b)
print ("A + 2:",a+2)
print ("B - 5.6:",b-5.6)
print ("A * 4:",a*5)
print ("B / 2", b / 2)
print ("A / B: ", a / b)

print("\n==================\n")

a = np.arange(1,10).reshape(3,3)
print("Elementos: ",a)
print("Soma dos elementos: ",np.sum(a))
print("Soma as linhas: ", np.sum(a,axis=0))
print("Média as linhas: ", np.average(a,axis=0))
print("Soma das colunas: ", np.sum(a,axis=1))
print("Média das colunas: ", np.average(a,axis=1))

print("\n==================\n")

a = np.array([0,0,1,1],dtype=np.bool8)
b = np.array([0,1,0,1], dtype=np.bool8)
print("A:", a)
print("B:", b)
print("A && B: ", a & b)
print("A || B: ", a | b)
print("~B: ", np.logical_not(b))
print("A^B: ", np.logical_xor(a,b))
 
print("\n==================\n")

a = np.arange(12).reshape((3,4))
b = np.arange(12).reshape((4,3))
print("A:", a)
print("B:", b)
print("A * B: ", a@b)
print("A * B: ", np.dot(a,b))
