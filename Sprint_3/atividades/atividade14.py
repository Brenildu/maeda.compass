# Escreva uma função que recebe um número variável de parâmetros não nomeados e um número variado de 
# parâmetros nomeados e imprime o valor de cada parâmetro recebido.

# Teste sua função com os seguintes parâmetros:
# (1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)


def func(*args, parametro_nomeado='alguma coisa', x=20):
    nao_nomeado = ''
    for arg in args:
        nao_nomeado += str(arg) + '\n'
    return f'{nao_nomeado}{parametro_nomeado}\n{x}'


if __name__ == '__main__':

    print(func(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20))   