# Leia o arquivo person.json, faça o parsing e imprima seu conteúdo.

# Dica: leia a documentação do pacote json

import json

if __name__ == '__main__':

    jason = open('person.json')

    if(jason):
        conteudo = json.loads(jason)
        print(conteudo)