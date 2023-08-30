# Exercícios Parte 1
# Desenvolva um código Python que lê do teclado nome e a 
# idade atual de uma pessoa. Como saída, imprima o ano em que a pessoa completará 100 anos de idade.

import datetime

def ano_100(idade):
    ano_nasc = datetime.datetime.now().year - idade
    return ano_nasc + 100

pessoa = {'nome': input(''), 'idade': int(input(''))}
print(f'{ano_100(pessoa["idade"])}')