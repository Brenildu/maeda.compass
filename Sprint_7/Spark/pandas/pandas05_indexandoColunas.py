# Indexando colunas
# Pode-se indexar colunas diretamente: df['NomeColuna'] ou múltiplas colunas df[['Col1', 'Col2']]
import pandas as pd

iris = pd.read_csv("./iris.csv")

print("indices de linhas: ", iris.index)
print("Colunas: ", iris.columns)
print(iris['sepal_length'])
print(iris[['petal_length', 'petal_width']])

# Indexando linhas
# Podemos indexar linhas de duas maneiras:
# utilizando df.loc[indice] caso o índice do dataframe não seja composto por inteiros
# utilizando df.iloc[indice] caso o índice do dataframe seja composto por inteiros
print("=======================")
print("Linhas 3, 9 e 36:", iris.iloc[[3,9,36]])
print("Linha 86:", iris.loc[86])
