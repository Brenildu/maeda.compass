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

def arredondar_notas(notas):
    return [round(nota) for nota in notas]

def tres_maiores(notas):
    return sorted(notas, reverse=True)[:3]

def processar_aluno(linha):
    colunas = linha.strip().split(',')
    nome_aluno = colunas[0]
    notas = [float(nota) for nota in colunas[1:]]

    notas_arredondadas = arredondar_notas(notas)
    
    tres_maiores_notas = tres_maiores(notas_arredondadas)
    media_tres_maiores = round(sum(tres_maiores_notas) / len(tres_maiores_notas), 2)
    
    aluno = {
        'Nome': nome_aluno,
        'Notas': tres_maiores_notas,
        'Média': media_tres_maiores
    }
    
    return aluno

try:
    with open('estudantes.csv') as arquivo:
        linhas = arquivo.readlines()

        alunos = list(map(processar_aluno, linhas))
        
        alunos_ordenados = sorted(alunos, key=lambda x: x['Nome'])
        
        for aluno in alunos_ordenados:
            print(f"Nome: {aluno['Nome']} Notas: {aluno['Notas']} Média: {aluno['Média']}")

except Exception as e:
    print(f"Ocorreu um erro: {e}")