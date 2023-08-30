PALAVRAS_PROIBIDAS = ('futebol', 'religiao', 'politica')
textos = (
    'Joao gosta de futebol e politica',
    'A praia estava legal hoje',
)

for texto in textos:
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print(f'O texto:{texto}\nAs seguintes palavras proibidas:{palavra}')
            break
    else:
        print(f'O texto:{texto} está aprovado')