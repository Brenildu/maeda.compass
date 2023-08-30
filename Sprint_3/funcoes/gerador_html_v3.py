#!C:\Users\breno\AppData\Local\Programs\Python\Python311\python.exe

# adição do tag_lista, a função será chamada no print dentro do tag_bloco 
# como substituição do texto se o mesmo for uma lista
def tag_bloco(conteudo, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{conteudo}</{tag}>'

# a cada vez que gerar novos valores irá ter a concatenação com a 
# string que começa vazia
def tag_lista(*itens):
    lista = ''.join((f'<li>{item}</li>' for item in itens))
    return f'<ul>{lista}</ul>'


if __name__ == '__main__':
    print(tag_bloco('bloco'))
    print(tag_bloco('inline e classe', 'info', True))
    print(tag_bloco('inline', inline=True))
    print(tag_bloco(inline=True, conteudo='inline'))  # ordem invertida
    print(tag_bloco('falhou', classe='error'))
    print(tag_bloco(tag_lista('Item 1', 'Item 2'), classe='info'))