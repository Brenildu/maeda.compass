def get_tipo_dia(dia):
    dias = {
        (1,7): 'Fim de Semana',
        tuple(range(2,7)): 'Dia de Semana'
    }

if __name__ == '__main__':
    generator = (get_tipo_dia(tipo_dia) for tipo_dia in range(1,7))
    
    for tipo in generator:
        print(generator)