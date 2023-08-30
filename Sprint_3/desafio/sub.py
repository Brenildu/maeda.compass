def substituir_ponto_por_exclamacao(texto):
    if ',' in texto:
        novo_texto = texto.replace(',', '!')
        return novo_texto
    else:
        return texto

entrada = input("Digite uma string: ")
resultado = substituir_ponto_por_exclamacao(entrada)
print("Resultado:", resultado)