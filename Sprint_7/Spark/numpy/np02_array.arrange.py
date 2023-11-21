# np.arange(...)
# Mesmo funcionamento da função range
# Várias assinaturas da função

import numpy as np 

a = np.arange(10)
b = np.arange(2,5)
c = np.arange(0,10,2)
d = np.arange(5,dtype=np.float32)

print("Conteúdo:{}, shape: {}, tipo: {}".format(a, a.shape, a.dtype))
print("Conteúdo:{}, shape: {}, tipo: {}".format(b, b.shape, b.dtype))
print("Conteúdo:{}, shape: {}, tipo: {}".format(c, c.shape, c.dtype))
print("Conteúdo:{}, shape: {}, tipo: {}".format(d, d.shape, d.dtype))
