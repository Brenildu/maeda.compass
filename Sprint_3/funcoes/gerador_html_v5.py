#!C:\Users\breno\AppData\Local\Programs\Python\Python311\python.exe

# definição de valores suportados
bloco_ats = ('bloco_acesskey', 'bloco_id')
ul_ats = ('ul_id', 'ul_style')


# adição da função filtrar
# só permite retornar os atributos que estão definidos em bloco_ats ou ul_ats
# a partir da string vazia é adicionado os atributos _ e uma tag
def filtrar_atrs(informados, suportados):
    return ' '.join(f'{k.split("_")[-1]}="{v}"'
                    for k, v in informados.items()  if k in suportados)


# adiciona uma das duas tags
# se conteudo for uma função html recebe seu return
# ao contrario recebe o valor de conteudo
# atributos recebe o return da função filtrar_atrs
def tag_bloco(conteudo, *args ,classe='success', inline=False, **novos_atrs):
    tag = 'span' if inline else 'div'
    html = conteudo if not callable(conteudo) \
        else conteudo(*args, **novos_atrs)
        
    atributos = filtrar_atrs(novos_atrs, bloco_ats)
    return f'<{tag} {atributos} class="{classe}">{html}</{tag}>'


# Opcional para listas ------------
# a cada vez que gerar novos valores irá ter a concatenação com a 
# string que começa vazia
def tag_lista(*itens, **novos_atrs):
    lista = ''.join((f'<li>{item}</li>' for item in itens))
    return f'<ul {filtrar_atrs(novos_atrs, ul_ats)}>{lista}</ul>'


if __name__ == '__main__':
    print(tag_bloco('bloco'))
    print(tag_bloco('inline e classe', classe='info', inline=True))
    print(tag_bloco('inline', inline=True))
    print(tag_bloco(inline=True, conteudo='inline'))  # ordem invertida
    print(tag_bloco('falhou', classe='error'))
    print(tag_bloco(tag_lista('Item 1', 'Item 2'), classe='info'))
    print(tag_bloco(tag_lista, 'Sabado', 'Domingo', classe='info', inline=True))
    print(tag_bloco(tag_lista, 'Item 1', 'Item 2', classe='info', 
                    bloco_accesskey='m', bloco_id='conteudo', ul_id='lista',
                    ul_style='color:red'))