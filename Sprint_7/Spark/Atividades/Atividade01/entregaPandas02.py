import pandas as pd
import numpy as np

def media_principais_filmes(data):
    data_unique = data.drop_duplicates(subset='#1 Movie', keep='first')
    data_sorted = data_unique.sort_values(by='Gross', ascending=False)
    top10_gross = data_sorted.head(10)['Gross']
    print(data_sorted)
    print("====")
    print(top10_gross)
    media = np.mean(top10_gross)
    return media

try:
    data = pd.read_csv('./actors.csv')
    media_receita = media_principais_filmes(data)
    print(f"A média de receita dos 10 filmes com maiores bilheterias é: {media_receita}")
    #with open('etapa-2.txt', 'w') as saida:
        #saida.write(f'A média dos 10 filmes com as maiores bilheterias é: {media}.\n')

finally:
    print("Finalizando!!")