# Utilizando high order functions, implemente o corpo da função conta_vogais. O parâmetro de entrada será uma string e o 
# resultado deverá ser a contagem de vogais presentes em seu conteúdo.

# É obrigatório aplicar as seguintes funções: len, filter, lambda
# Desconsidere os caracteres acentuados. Eles não serão utilizados nos testes do seu código.
def conta_vogais(palavra):
    palavra = palavra.lower()
    
    vogais = lambda c: c in 'aeiou'
    
    vogais_palavra = filter(vogais, palavra)

    num_vogais = len(list(vogais_palavra))
    
    return num_vogais


palavra = "ola mundo"
print(conta_vogais(palavra))