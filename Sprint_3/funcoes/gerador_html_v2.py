#!C:\Users\breno\AppData\Local\Programs\Python\Python311\python.exe

# já vem preenchido os ultimos dois parametros
# adição de tag personalizada por ser de linha ou não
def tag_bloco(texto, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{texto}</{tag}>'

if __name__ == '__main__':
    print(tag_bloco('bloco'))
    print(tag_bloco('inline e classe', 'info', True))
    print(tag_bloco('inline', inline=True))
    print(tag_bloco(inline=True, texto='inline'))  # ordem invertida
    print(tag_bloco('falhou', classe='error'))