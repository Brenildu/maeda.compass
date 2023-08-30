#!C:\Users\breno\AppData\Local\Programs\Python\Python311\python.exe
with open('pessoas.csv') as arquivo:

    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.split(',')))


if arquivo.closed:
    print('Arquivo ja foi fechado')