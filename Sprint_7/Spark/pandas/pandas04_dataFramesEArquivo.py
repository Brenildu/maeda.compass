# Da mesma forma que é possível criar dataframes a partir do conteúdo de arquivos, também podemos escrever arquivos a partir de 
# dataframes. É o caso do exemplo a seguir, no qual escrevemos um arquivo parquet a partir de um subconjunto do dataframe iris
import pandas as pd

iris = pd.read_csv("./iris.csv")

output = iris.loc[4:10, ['sepal_length', 'sepal_width']]
print(output)
output.to_parquet("./iris.parquet")