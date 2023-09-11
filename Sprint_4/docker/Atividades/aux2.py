# Um determinado sistema escolar exporta a grade de notas dos estudantes em formato CSV. Cada 
# linha do arquivo corresponde ao nome do estudante, acompanhado de 5 notas de avaliação, no 
# intervalo [0-10]. É o arquivo estudantes.csv de seu exercício.

#Precisamos processar seu conteúdo, de modo a gerar como saída um relatório em formato textual contendo as seguintes informações:
#Nome do estudante
# Três maiores notas, em ordem decrescente
# Média das três maiores notas, com duas casas decimais de precisão
# O resultado do processamento deve ser escrito na saída padrão (print), ordenado pelo nome do estudante e obedecendo ao formato descrito a seguir:

# Nome: <nome estudante> Notas: [n1, n2, n3] Média: <média>

# Exemplo:
# Nome: Maria Luiza Correia Notas: [7, 5, 5] Média: 5.67
# Nome: Maria Mendes Notas: [7, 3, 3] Média: 4.33

# Em seu desenvolvimento você deverá utilizar lambdas e as seguintes funções:
# round
# map
# sorted

import csv

def calcular_media_tres_maiores(notas):
    media = sum(notas) / len(notas)
    return round(media, 2)

def tres_maiores(notas):
    return sorted(notas, reverse=True)[:3]

def processar_estudantes(linhas):
    alunos = []
    
    for linha in linhas:
        colunas = linha.strip().split(',')
        nome_aluno = colunas[0]
        notas = [float(nota) for nota in colunas[1:]]
        
        tres_maiores_notas = tres_maiores(notas)
        media_tres_maiores = calcular_media_tres_maiores(tres_maiores_notas)
        
        aluno = {
            'Nome': nome_aluno,
            'Notas': tres_maiores_notas,
            'Média': media_tres_maiores
        }
        
        alunos.append(aluno)
    
    # Ordenar alunos pelo nome
    alunos_ordenados = sorted(alunos, key=lambda x: x['Nome'])
    
    # Imprimir o relatório
    for aluno in alunos_ordenados:
        print(f"Nome: {aluno['Nome']} Notas: {aluno['Notas']} Média: {aluno['Média']}")

try:
    with open('estudantes.csv') as arquivo:
        linhas = arquivo.readlines()
        processar_estudantes(linhas)

except FileNotFoundError:
    print("O arquivo 'estudantes.csv' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")