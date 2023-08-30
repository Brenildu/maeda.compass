# for i in range(1, 10):
#    if i == 6:
#        break
#    print(i)
#else:
#    print('Fim')


# Função sortear_dado ,6 números entre 1 e 6
# For com range 1 a 6
# Se for impar continue
# se for par e for igual ao valor sorteado pela funcao
# dado ao imprimir 'ACERTOU' e depois chamar o break
# se não acertar chama o else, printa não acertou   

from random import randint

def sortear_dado():
    return randint(1,6)


for i in range(1,7):
    if i % 2 == 1:
        continue
    
    if sortear_dado() == i:
        print('ACERTOU!', i)
        break
else:
    print('Não acertou')    

