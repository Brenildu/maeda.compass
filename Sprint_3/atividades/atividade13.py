# Implemente a função my_map(list, f) que recebe uma lista como primeiro argumento e uma função como segundo argumento.
# Esta função aplica a função recebida para cada elemento da lista recebida e retorna o resultado em uma nova lista.



# Teste sua função com a lista de entrada [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] e com uma função que potência de 2 para cada elemento.


def my_map(lst, f):
    if callable(f):
        nova_lista = f(lst)
        print(nova_lista)

def potencia(lst):
    nova_lista = []
    for num in lst:
        nova_lista.append(num*num)
    return nova_lista

if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    my_map(lista, potencia)