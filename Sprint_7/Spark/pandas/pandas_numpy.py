# A qualquer momento podemos converter os dados para Numpy utilizando a propriedade de DataFrames e Series utilizando o método .values.
import pandas as pd
import numpy as np

df = pd.DataFrame(data=np.random.random((5,5)), index=['a','b','c','d','e'], columns=['k','l','m','n','o'])

np_array = df.values

print(np_array)
print(type(np_array), np_array.shape, np_array.dtype)

print("================")

# Ordenação, Agregação, Junção e Split
# Assim como NumPy, Pandas também suporta ordenação de linhas/colunas. A ordenação mantém a integridade das linhas/colunas.
# Ordena as linhas
df2 = pd.DataFrame(data=np.random.random((5,5)), index=['a','b','c','d','e'], columns=['k','l','m','n','o'])

df2.sort_values(by="0", axis=0)
print(df2)


print("================")

# Ordena as colunas
df2.sort_values(by="b", axis=1)
print(df2)

print("================")

# Função map
# pandas.DataFrame.apply
# Semelhante a função nativa de Python
# Aplica uma função a cada uma das linhas ou colunas de um DataFrame


def negativo_se_par(row):
    for c in ['k','l','m','n','o']:
        if row[c]%2 == 0:
            row[c]=-row[c]

df.apply(negativo_se_par, axist=1)

print(df)