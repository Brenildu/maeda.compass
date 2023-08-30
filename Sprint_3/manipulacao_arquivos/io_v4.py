#!C:\Users\breno\AppData\Local\Programs\Python\Python311\python.exe
try:
    arquivo = open('pessoas.csv')

    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.split(',')))
finally:
    print('finally')
    arquivo.close()

if arquivo.closed:
    print('Arquivo ja foi fechado')