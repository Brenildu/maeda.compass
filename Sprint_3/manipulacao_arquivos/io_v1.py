#!C:\Users\breno\AppData\Local\Programs\Python\Python311\python.exe
arquivo = open('pessoas.csv')
dados = arquivo.read()
arquivo.close()
for registro in dados.splitlines():
    #print(*registro.split(','))
    #print('Nome: {}, Idade: {}'.format(*registro.split(',')))
    nome, idade = registro.split(',')
    print('Nome: {}, Idade: {}'.format(nome, idade), end=' ')