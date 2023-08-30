class Calculo:
    def soma(self, x, y):
        return x + y

    def subtracao(self, x, y):
        return x - y

# Valores de teste
x = 4
y = 5

calculo = Calculo()
soma_resultado = calculo.soma(x, y)
subtracao_resultado = calculo.subtracao(x, y)

print(f'Somando: {x}+{y} = {soma_resultado}')
print(f'Subtraindo: {x}-{y} = {subtracao_resultado}')