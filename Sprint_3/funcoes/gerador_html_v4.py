#!C:\Users\breno\AppData\Local\Programs\Python\Python311\python.exe

# adição de *args que será capturado como uma tupla e variavel html 
def tag_bloco(conteudo, *args ,classe='success', inline=False):
    tag = 'span' if inline else 'div'

    # html recebe um texto ou um resultado de uma função aonde os parametros são os args
    html = conteudo if not callable(conteudo) else conteudo(*args)
    return f'<{tag} class="{classe}">{html}</{tag}>'

# a cada vez que gerar novos valores irá ter a concatenação com a 
# string que começa vazia
def tag_lista(*itens):
    lista = ''.join((f'<li>{item}</li>' for item in itens))
    return f'<ul>{lista}</ul>'


if __name__ == '__main__':
    print(tag_bloco('bloco'))
    print(tag_bloco('inline e classe', classe='info', inline=True))
    print(tag_bloco('inline', inline=True))
    print(tag_bloco(inline=True, conteudo='inline'))  # ordem invertida
    print(tag_bloco('falhou', classe='error'))
    # conteudo = texto
    print(tag_bloco(tag_lista('Item 1', 'Item 2'), classe='info'))
    # conteudo = funcao   +   *args
    print(tag_bloco(tag_lista, 'Sabado', 'Domingo', classe='info', inline=True))