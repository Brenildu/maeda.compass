# Uniao
# pandas.DataFrame.merge
# Permite unir os registros de duas tabelas sem que seja necessário fazer um join
# Insere NaN nas colunas que não são compartilhadas entre as duas tabelas
# Vamos considerar os seguintes dataframes:
import pandas as pd
import numpy as np

cidades = pd.DataFrame(
    {
        'cidade_id':[1,2,3,4,5],
        'cidade_nome':['Cidade A', 'Cidade B','Cidade C','Cidade D','Cidade E']
    }
)
estudantes = pd.DataFrame(
    {
        'estudante_id': [1,2,3,4,5],
        'estudante_nome':['Estudante A','Estudante B','Estudante C','Estudante D','Estudande E'],
        'cidade_id':[2,3,3,5,6]
    }
)
print(cidades)
print(estudantes)

print("============")

# Para realizarmos merge com estratégia inner podemos utilizar:
pd.merge(cidades, estudantes,how="inner")
print(pd)

print("============")

# E, para estratégia de right outer join podemos utilizar:

pd.merge(cidades, estudantes,how="right")
print(pd)

print("==========================")

# Por fim, para informar o nome das colunas que formam o critério de junção, utilizamos o parâmetro on, left_on e right_on
pd.merge(cidades, estudantes,how="right", left_on='cidade_id', right_on='estudante_id')

# Agrupamento
# pandas.DataFrame.groupby
# Opera sob o mesmo princípio de um group by de um banco de dados relacional: agrupa dados utilizando um atributo como pivô

estudantes = pd.DataFrame(
    {
        'estudante_id': [1,2,3,4,5],
        'estudante_nome':['Estudante A','Estudante B','Estudante C','Estudante D','Estudande E'],
        'cidade_id':[2,3,3,5,6],
        'cor_pele':['branco','preto','preto','pardo','branco']
    }
)
estudantes.groupby(by='cor_pele').count()

# Método agg
#Permite agregar dados usando uma ou mais operações sobre algum eixo. No exemplo abaixo usando uma medida de média aritmética do NumPy

estudantes = pd.DataFrame(
    {
        'estudante_id': [1,2,3,4,5],
        'estudante_nome':['Estudante A','Estudante B','Estudante C','Estudante D','Estudande E'],
        'cidade_id':[2,3,3,5,6],
        'cor_pele':['branco','preto','preto','pardo','branco'],
        'nota_redacao':[9,8,8.6,7,6]
    }
)
estudantes.agg({'nota_redacao':[np.mean,np.median,np.std]})