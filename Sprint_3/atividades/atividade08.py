# Exercícios Parte 2
# Verifique se cada uma das palavras da lista ['maça', 'arara', 'audio', 'radio', 'radar', 'moto'] é ou não um palíndromo.

# Obs: Palíndromo é uma palavra que permanece igual se lida de traz pra frente.
# É necessário que você imprima no console exatamente assim:
# A palavra: maça não é um palíndromo
# A palavra: arara é um palíndromo
# A palavra: audio não é um palíndromo
# A palavra: radio não é um palíndromo
# A palavra: radar é um palíndromo
# A palavra: moto não é um palíndromo


if __name__ == '__main__':
    lista = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']

    for i in lista:
        palavra = i
        varA = 0
        varb = 0
        tamanho = len(palavra) - 1
        while tamanho >= varA:

            if palavra[varA] !=  palavra[tamanho]:
                varb += 1
            varA += 1
            tamanho -= 1
        
        if(varb):
            print(f'A palavra: {palavra} não é um palíndromo')
        else:
            print(f'A palavra: {palavra} é um palíndromo')