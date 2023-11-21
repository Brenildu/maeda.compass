# np.array(...)
# Constrói um array com base nos dados que são passados à estrutura
# Dados podem ser provenientes de outros contêineres (lista, tupla), conforme demonstramos no código abaixo

import numpy as np
tupla = ('a', 'b', 'c','d')
lista = [1,3,6,9,7,9,12]
array1 = np.array(tupla)
array2 = np.array(lista)

print("Conteúdo:{}, shape: {}, Tipo: {} ".format(array1, array1.shape, array1.dtype))
print("Conteúdo:{}, shape: {}, Tipo: {} ".format(array2, array2.shape, array2.dtype))

array3 = np.array(lista,dtype=np.float32)
print("Conteúdo:{}, shape: {}, Tipo: {} ".format(array3, array3.shape, array3.dtype))
