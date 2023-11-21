# DataFrame
# É a principal estrutura de dados do Pandas
# Representa uma tabela similar às tabelas de bancos de dados relacionais
# Permite dados heterogêneos (uma coluna do tipo float, outra do tipo str, por exemplo)
# Permite operações semelhantes a operações de banco de dados (Seleção, agregação, etc...
import pandas as pd

df = pd.DataFrame(
     [
         ['a','b','c'],
         ['d',4,5],
         [6,7,8]
     ],
index=['linha 0','linha 1','linha 2'],
columns = ['coluna 0','coluna 1','coluna 2'],
copy = True
)

print(df)