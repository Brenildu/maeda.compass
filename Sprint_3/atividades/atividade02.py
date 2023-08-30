numeros = []

for _ in range(3):
    numero = int(input(''))
    tipo = 'Par' if numero % 2 == 0 else 'Ímpar'
    numeros.append({'tipo': tipo, 'numero': numero})

for item in numeros:
    print(f'{item["tipo"]}: {item["numero"]}')