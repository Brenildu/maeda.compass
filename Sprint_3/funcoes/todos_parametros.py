def todos_params(*args, **kwargs):
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')


if __name__ == '__main__':
    todos_params('a', 'b', 'c') # apenas parametros posicionais
    todos_params(1, 2, 3, legal=True, valor=12.99) # parametros posicionais e nomeados
    todos_params('Ana', False, [1, 2, 3], tamanho='M', fragil=False)
    todos_params(primeiro='Joao', segundo='Maria')
    todos_params('Maria', primeiro='Joao')