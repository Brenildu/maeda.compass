#Você está recebendo um arquivo contendo 10.000 números inteiros, um em cada linha. Utilizando lambdas e high order functions, 
#apresente os 5 maiores valores pares e a soma destes.

# Você deverá aplicar as seguintes funções no exercício: map ,filter, sorted, sum
#Seu código deverá exibir na saída (simplesmente utilizando 2 comandos `print()`):
#a lista dos 5 maiores números pares em ordem decrescente;
#a soma destes valores.

try:
    with open('number.txt') as arquivo:
        numeros = []
        arq = arquivo.readlines()
        numeros = lambda num: num, int(arq.strip)
        #for num in arq:
        #    numeros.append(int(num.strip()))

        numeros_pares = filter(lambda x: x % 2 == 0, numeros)
        
        numeros_pares_ordenados = sorted(numeros_pares, reverse=True)

        cinco_maiores = list(map(lambda x: x, numeros_pares_ordenados[:5]))
        print(cinco_maiores)

        soma_cinco_maiores = sum(cinco_maiores)
        print(soma_cinco_maiores)

finally:
    pass