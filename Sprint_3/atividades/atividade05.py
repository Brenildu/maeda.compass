# Escreva um código Python que declara 3 variáveis:
#   dia, inicializada com valor 22
#   mes, inicializada com valor 10 e
#   ano, inicializada com valor 2022
#Como saída, você deverá imprimir a data correspondente, no formato a seguir dia/mes/ano.
def imprime_data(dia=22, mes=10, ano=2022):
    if dia>0 and dia<32 and mes>0 and mes<13 and ano> 2000:
        print(f'{dia}/{mes}/{ano}')

if __name__ == '__main__':
    imprime_data()