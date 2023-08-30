#Escreva um código Python para imprimir todos os números primos entre 1 até 100. 
# Lembre-se que você deverá desenvolver o cálculo que identifica se um número é primo ou não.
# Importante: Aplique a função range().

if __name__ == '__main__':

    for num in range(1, 101):
        div = 0
        for aux in range(1, num+1):
            if num % aux == 0:
                div = div + 1
            if div > 2:
                continue
        if div == 2:
            print(f'- {num}')