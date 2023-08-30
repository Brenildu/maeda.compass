# Escreva um programa que lê o conteúdo do arquivo texto arquivo_texto.txt e imprime o seu conteúdo.

# Dica: leia a documentação da função open(...)

if __name__ == '__main__':
    
    try:
        arquivo = open('arquivo_texto.txt')

        toString = ''
        for conteudo in arquivo:
            toString = toString + ' ' + conteudo

        print(toString)
    finally:
        print('finally')
        arquivo.close()