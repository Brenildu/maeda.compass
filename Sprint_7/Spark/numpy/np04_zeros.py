# np.zeros(…) e np.ones(…)
# Constrói arrays onde todos os valores são 0 ou 1

import numpy as np

zeros = np.zeros((3,3),dtype=np.int16)
ones = np.ones((3,2),dtype=np.int16)

print("Conteúdo:{}, shape: {}, Tipo: {} ".format(zeros, zeros.shape, zeros.dtype))
print("Conteúdo:{}, shape: {}, Tipo: {} ".format(ones, ones.shape, ones.dtype)),