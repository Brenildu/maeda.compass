# Seleção
# A seleção em pandas é similar ao que ocorre em bancos de dados relacionais
# É possível selecionar valores com base no valor de diversas colunas, simultaneamente. Vamos considerar o seguinte dataframe em nosso 
# exemplo:

import pandas as pd
import numpy as np

df = pd.DataFrame(data=np.random.random((5,5)), index=['a', 'b', 'c', 'd', 'e'], columns=['k', 'l', 'm', 'n', 'o'])

print(df)

print("================")
#Linhas em que o valor da coluna k é maior que 0.5 E coluna o possui valor maior que 0.6

linhas_colunas_maior = [(df['k'] > 0.5) & (df['o'] > 0.6)]
print(linhas_colunas_maior)

print("================")
#Linhas em que o valor da coluna k é maior que 0.5 OU coluna o possui valor maior que 0.8

linhas_colunas_menor = [(df['k'] > 0.5) | (df['o'] > 0.8)]
print(linhas_colunas_menor)

print("================")

# A estrutura loc também aceita indexação por linhas e colunas. Primeiro informa-se a linha desejada, e depois o nome da coluna. Observe:
seleciona_a = df.loc['a']
print(seleciona_a)

print("================")

# Seleciona as linhas a e b e as colunas x e y
selecia_abEkl = df.loc[['a', 'b'], ['k', 'l']]
print(selecia_abEkl)

print("================")

