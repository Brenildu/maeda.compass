# Escreva uma função que recebe uma string de números separados por vírgula e retorne a soma de todos eles. 
# Depois imprima a soma dos valores.

# A string deve ter valor  "1,3,4,6,10,76"

def soma_seq(texto):
    
    seq = []
    numeros = texto.split(',')
    for num in numeros:
        seq.append(int(num))


    soma = 0
    for num in seq:
        soma = soma + num

    return soma
    

if __name__ == '__main__':

    print(f' {soma_seq("1,3,4,6,10,76")}')