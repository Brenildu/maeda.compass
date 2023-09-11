import hashlib

continuar = True
while continuar:
    input_string = input("Escreva uma string(ou digite 's' para sair): ")

    if input_string.lower() == 's':
        continuar = False
        print('Finalizando!!')
        continue

    sha1_hash = hashlib.sha1(input_string.encode()).hexdigest()

    print("Hash SHA-1 da string:", sha1_hash)