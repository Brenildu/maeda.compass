#!C:\Users\breno\AppData\Local\Programs\Python\Python311\python.exe
arquivo = open('pessoas.csv')

for registro in arquivo:
    print('Nome: {}, Idade: {}'.format(*registro.split(',')), end='')
    
arquivo.close()