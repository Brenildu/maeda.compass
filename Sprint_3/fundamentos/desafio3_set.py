PALAVRAS_PROIBIDAS = {'futebol', 'religiao', 'politica'} # set
textos = (
    'Joao gosta de futebol e politica',
    'A praia estava legal hoje',
) #tuplas

for texto in textos:
    intersecao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
    if intersecao:
            print('Tem palavra probida', intersecao)
    else:
        print('Não tem palavra probida')