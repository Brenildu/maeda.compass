# Exercícios Parte 2
# Dada a seguinte lista:
# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# Faça um programa que gere uma nova lista contendo apenas números ímpares.

if __name__ == '__main__':
    
    impares =  (num*num for num in range(11) if num % 2 == 1)

    lista = []
    for i in impares:
        lista.append(i)

    print(lista)