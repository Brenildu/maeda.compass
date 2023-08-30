#Dada as listas a seguir:
# primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
# sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
# idades = [19, 28, 25, 31]

# Faça um programa que imprima o dados na seguinte estrutura: "índice - primeiroNome sobreNome está com idade anos".

# Exemplo:

# 0 - João Soares está com 19 anos

if __name__ == '__main__':
    primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
    sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
    idades = [19, 28, 25, 31]

    for indice, idade in enumerate(idades):
        print(f'{indice} - {primeirosNomes[indice]} {sobreNomes[indice]} está com {idade} anos')