PALAVRAS_PROIBIDAS = ('futebol', 'religião', 'politica')
textos = {
    'João gosta de futebol e politica',
    'A praia foi divertida',
}

for texto in textos:
    found = False
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print(f'O Texto: {texto}\n possui pelo menos uma palavra proibida: {palavra}')
            found = True
            break

    if not found:
        print('Texo autorizado:', texto)