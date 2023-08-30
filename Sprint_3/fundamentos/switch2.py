def get_tipo_dia(dia):
    dias = {
        1: 'Dia de semana',
        2: 'Dia de semana',
        3: 'Dia de semana',
        4: 'Dia de semana',
        5: 'Final de semanana',
        6: 'Final de semanana',
        7: 'Final de semanana',
    }
    return dias.get(dia ,'** Dia inválido **')


if __name__ == '__main__':
    for dia in range(1, 8):
        print(f'{dia} : {get_tipo_dia(dia)}')