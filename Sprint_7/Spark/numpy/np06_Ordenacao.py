#Existem diversos algoritmos disponíveis para ordenação na biblioteca NumPy, dentre eles:
# Quicksort
# Mergesort
# Heapsort

import numpy as np 


a = np.random.choice(30,size=10, replace=False)
print("A: ",a)
print("A ordenado com quicksort",np.sort(a))
print("A ordenado com mergesort",np.sort(a,kind="mergesort"))

print("\n==================\n")

a = np.random.choice(30,size=(5,5), replace=False)
print("A: ",a)
print("A ordenado por linha",np.sort(a,axis=1))
print("A ordenado por coluna",np.sort(a,axis=0))
