#!C:\Users\breno\AppData\Local\Programs\Python\Python311\python.exe

# o pop vai pegar e substituir as chaves html-class para class
# k = chave v = valores, kwargs dicionario
def tag(tag, *args, **kwargs):
    if 'html_class' in kwargs:
        kwargs['class'] = kwargs.pop('html_class')
    attrs = ' '.join(f'{k}="{v}"' for k, v in kwargs.items())
    inner = ' '.join(args)
    return f'<{tag} {attrs}> {inner}</{tag}>'


if __name__ == '__main__':
    print(
        tag('p',
            tag('span', 'Curso Python 3, por'),
            tag('strong', 'Juracy Filho', id='jf'),
            tag('span', ' e '),
            tag('strong', 'Leonardo Leitão', id='ll'),
            tag('span', '.'),
            html_class='alert')
    )