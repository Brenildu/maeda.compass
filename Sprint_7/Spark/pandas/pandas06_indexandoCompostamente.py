# Indexação composta
# A indexação padrão dos dataframes assume apenas um valor por índice
# Todavia, é possível utilizar índices compostos
# Útil quando estamos visualizando informações agregadas

import pandas as pd

index = pd.MultiIndex.from_tuples([("2018", "ka"), ("1980", "Fusca"),("2014","ka")], names=["ano", "modelo"])

df = pd.DataFrame(
    data = [[4, 50000], [2, 5000], [2, 15000]],
    index = index,
    columns = ['Nr portas', 'Valor']
)                     

print(df.loc[[('1980', 'Fusca'), ('2014', 'ka')]])