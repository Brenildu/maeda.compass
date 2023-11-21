import pandas as pd
import numpy as np

def ator_com_mais_filmes():
    data = pd.read_csv("./actors.csv")
    print(data)
    max_number_of_movies = data['Number of Movies'].max()
    actor_max = data.loc[data['Number of Movies'] == max_number_of_movies, 'Actor/Actress'].values[0]

    return actor_max, max_number_of_movies


try:
    ator, quantidade_filmes = ator_com_mais_filmes()

    with open('etapa-1.txt', 'w') as saida_1:
        saida_1.write(f"O ator/atriz com maior número de filmes é {ator} com {quantidade_filmes} filmes.\n")
        
finally:
    print('Finalizando')