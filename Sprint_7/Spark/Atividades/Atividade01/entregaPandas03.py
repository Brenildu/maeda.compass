import pandas as pd

def atores_com_maior_media_bilheteria(data):
    data_sorted = data.sort_values(by='Average per Movie', ascending=False)
    top10_data = data_sorted.head(10)
    atores = top10_data['Actor'].tolist()
    medias = top10_data['Average per Movie'].tolist()
    return atores, medias

try:
    data = pd.read_csv('actors.csv')
    atores, medias = atores_com_maior_media_bilheteria(data)

    with open('etapa-3.txt', 'w') as saida:
        toString = 'Atores com maiores médias de bilheterias: ' + '\n'
        for indice, (ator, media) in enumerate(zip(atores, medias), 1):
            toString += f'{indice}- {ator}: {media}\n'

        print(toString)
        saida.write(toString)

finally:
    print("Finalizando!!!")