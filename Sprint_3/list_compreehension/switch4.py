def get_tipo_dia(dia):
    dias = {
        (1,7): 'Fim de Semana',
        tuple(range(2,7)): 'Dia de Semana'
    }
    # um generator que percorre o dicionario, retornando tipo se ele estiver dentro de numero
    dia_escolhido = (tipo for numeros, tipo in dias.items() if dia in numeros)
    # se não encontrar ele retorna um valor invalido
    return next(dia_escolhido, '** dia inválido **')

if __name__ == '__main__':
    # até 8 para testar se o dia invalido esta dando certo
    for dia in range(1,9):
        print(f'{dia} : {get_tipo_dia(dia)}')