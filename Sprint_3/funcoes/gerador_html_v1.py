#!C:\Users\breno\AppData\Local\Programs\Python\Python311\python.exe
 # é obrigado a passar pelo menos o parametro de texto, o de classe ja vem preenchido
def tag_bloco(texto, classe='success'):
    return f'<div class="{classe}">{texto}</div>'

if __name__ == '__main__':
    # testes (assertions)
    print (tag_bloco('Incluído com sucesso!')) == \
        '<div class="success">Incluído com sucesso!</div>'
    print (tag_bloco('Impossível excluir', 'error')) == \
        '<div class="error">Impossível excluir</div>'
    print(tag_bloco('bloco'))