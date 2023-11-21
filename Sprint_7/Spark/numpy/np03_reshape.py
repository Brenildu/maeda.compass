# Alterando as dimensões de um array (reshape)

import numpy as np

vector = np.arange(stop=20, dtype=np.int16)
print("Conteúdo:{}, shape: {}, Tipo: {} ".format(vector, vector.shape, vector.dtype))

matrix = vector.reshape((5,4))
print("Conteúdo:{}, shape: {}, Tipo: {} ".format(matrix, matrix.shape, matrix.dtype))

cube = vector.reshape((5,2,2))
print("Conteúdo:{}, shape: {}, Tipo: {} ".format(cube, cube.shape, cube.dtype))

