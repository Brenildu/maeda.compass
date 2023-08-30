# Actor: Nome do ator.
# Total Gross:  Receita bruta de bilheteria doméstica, em milhões de dólares, de todos os fi'lmes do ator.
# Number of movies: Número de filmes em que o ator participou
# Average per Movie: Corresponde à bilheteria bruta dividida pelo número de filmes
#1 Movie: Filme de maior receita bruta em que o ator participou
# Gross: Receita bruta de bilheteria doméstica, em milhões de dólares, do filme de maior receita.

# Perguntas dessa tarefa:

# 1 Apresente o ator/atriz com maior número de filmes e a respectiva quantidade.
def split_manual(linha):
    
    nova_linha = []
    dentro_da_string = False
    parte_atual = ""

    # laço que vai percorrer a linha inteira e verificar se possui virgula fora de alguma string
    # se possuir fora entedemos que é uma nova coluna e adicionamos o valor da coluna na lista nova_linha[] com o metodo append 
    # se for dentro é entendido que ela faz parte do valor assim podemos manipular strings com virgulas
    for char in linha:
        if char == '"':
            dentro_da_string = not dentro_da_string   # a primeira aparição entra na string e a segunda sai
        elif char == ',' and  dentro_da_string == False:
            nova_linha.append(parte_atual)
            parte_atual = ""
        else:
            parte_atual += char

    nova_linha.append(parte_atual.strip()) # transformo em coluna aqui
    return nova_linha 


def ator_com_mais_filmes(linhas):
    max_number_of_movies = 0
    actor_max = None

    # laço que percorre linha por linha e separa as colunas sem usar o metodo split() e sim uma função que devolve as colunas separadas com o strip
    for linha in linhas:
        colunas = split_manual(linha)
        number_of_movies = int(colunas[2])

        if number_of_movies > max_number_of_movies:
            max_number_of_movies = number_of_movies
            actor_max = colunas[0]

    return actor_max, max_number_of_movies


# 2 Apresente a média de receita de bilheteria bruta dos principais filmes
def media_principais_filmes(linhas):
    gross_ordenado = []
    filmes = []

    for linha in linhas:
        colunas = split_manual(linha)

        if(not colunas[4] in filmes):
            filmes.append(colunas[4])
            gross = float(colunas[5])
            gross_ordenado.append(gross)

    gross_ordenado = sorted(gross_ordenado, reverse=True)
    top10_gross = gross_ordenado[:10]
    
    media = sum(top10_gross) / 10
    return media


# 3 Apresente o ator/atriz com a maior média de receita de bilheteria bruta por filme do conjunto de dados. 
#Considere a coluna Avarage per Movie para fins de cálculo.
def atores_com_maior_media_bilheteria(linhas):
    maiores_medias = []
    atores = []
    top10_medias = []

    for linha in linhas:
        colunas = split_manual(linha)

        media = float(colunas[3])
        maiores_medias.append(media)

    # encontro as maiores médias para depois retornar os nomes dos atores que as detêm
    maiores_medias = sorted(maiores_medias, reverse=True)
    top10_medias = maiores_medias[:10]

    # pensei em usar uma função para percorrer as linhas mas fiquei sem tempo :( essa foi a forma mais simples que pensei
    # laços aninhados que vão percorrer todas as medias e comparar com as medias do top10, a ideia é pegar o nome dos atores pela comparação
    for media in top10_medias:
        for linha in linhas:
            colunas = split_manual(linha)
            if float(colunas[3]) == media:
                atores.append(colunas[0])

    return atores, top10_medias


# 4 A coluna #1 Movie contém o filme de maior bilheteria em que o ator atuou. 
#Realize a contagem de aparições destes filmes no dataset, listando-os ordenados pela quantidade de vezes em que estão presentes. Considere a ordem decrescente e, em segundo nível, o nome do  filme.


# Ao escrever no arquivo, considere o padrão de saída <sequencia> - O filme <nome filme> aparece <quantidade> vez(es) no dataset, adicionando um resultado a cada linha.
def contagem_aparicoes(linhas):
    todos_filmes = []
    filmes_nao_repitidos = []
    contagem = [] 

    for linha in linhas:
        colunas = split_manual(linha)
        todos_filmes.append(colunas[4])

    for filme in todos_filmes:
        if filme not in filmes_nao_repitidos:
            filmes_nao_repitidos.append(filme)
            cont = {'quantidade': 1, 'nome filme': filme}
            contagem.append(cont)
        else:
            for cont in contagem:
                if filme == cont['nome filme']:
                    cont['quantidade'] += 1

    return contagem


# 5 Apresente a lista dos atores ordenada pela receita bruta de bilheteria de seus filmes (coluna Total Gross), em ordem decrescente.
# Ao escrever no arquivo, considere o padrão de saída <nome do ator> -  <receita total bruta>, adicionando um resultado a cada linha.
def lista_atores_pela_receita_bruta(linhas):
    total_gross = []
    atores = []

    for linha in linhas:
        colunas = split_manual(linha)

        gross = float(colunas[1])
        total_gross.append(gross)

    total_gross = sorted(total_gross, reverse=True)

    for gross in total_gross:
        for linha in linhas:
            colunas = split_manual(linha)
            if float(colunas[1]) == gross:
                nome_ator = colunas[0]
                ator = {'nome ator': nome_ator, 'receita': gross}
                atores.append(ator)

    return atores


try:
    with open('actors.csv') as arquivo:
        dados = arquivo.readlines()
        header = dados[0]
        linhas = dados[1:]


        with open('etapa-1.txt', 'w') as saida_1:
            ator, quantidade_filmes = ator_com_mais_filmes(linhas)

            saida_1.write(f"O ator/atriz com maior número de filmes é {ator} com {quantidade_filmes} filmes.\n")
        
        with open('etapa-2.txt', 'w') as saida_2:
            media = media_principais_filmes(linhas)

            saida_2.write(f'A média dos 10 filmes com as maiores bilheterias é: {media}.\n')

        with open('etapa-3.txt', 'w') as saida_3:
            atores, medias = atores_com_maior_media_bilheteria(linhas)
            toString = 'Atores com maiores médias de bilheterias: ' + '\n'
            for indice in range(10):
                toString += f'{indice+1}- {atores[indice]}: {medias[indice]}\n'

            saida_3.write(toString)

        with open('etapa-4.txt', 'w') as saida_4:
            filmes = contagem_aparicoes(linhas)
            filmes_ordenados = sorted(filmes, key=lambda x: x['quantidade'], reverse=True)
            seq = 1
            for filme_info in filmes_ordenados:
                filme = filme_info['nome filme']
                quantidade = filme_info['quantidade']
                saida_4.write(f'{seq}- O filme "{filme}" aparece {quantidade} vez(es) no dataset.\n')
                seq += 1

        with open('etapa-5.txt', 'w') as saida_5:
            atores = lista_atores_pela_receita_bruta(linhas)
            toString = ''
            atores_ordenados_receita = sorted(atores, key=lambda y: y['receita'], reverse=True)
            seq = 1
            for ator_info in atores_ordenados_receita:
                ator = ator_info['nome ator']
                receita = ator_info['receita']
                saida_5.write(f'{seq}- {ator} - {receita}.\n')
                seq += 1
                
finally:
    print('Finalizando')

