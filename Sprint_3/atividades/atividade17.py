# Escreva uma função que recebe como parâmetro uma lista e retorna 3 listas: a lista recebida dividida em 3 partes iguais. 
# Teste sua implementação com a lista abaixo

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def divide_lista(lista):
    original = lista
    lista1 = []
    lista2 = []
    lista3 = []
    tam1 = int(len(lista)/3)
    tam2 = int(len(lista))- tam1
    tam3 = int(len(lista))
    
    for num in range(tam1):
        lista1.append(original[num])
    
    for num in range(tam1, tam2):
        lista2.append(original[num])

    for num in range(tam2, tam3):
        lista3.append(original[num])   

    print(f'{lista1} {lista2} {lista3}')

if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    divide_lista(lista)