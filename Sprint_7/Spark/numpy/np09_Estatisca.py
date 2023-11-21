import numpy as np

valores = np.random.randint(0,20, size=10)
valores.sort()
print("Valores:", valores)
print("Média aritmética: ",np.mean(valores))
print("Mediana: ",np.median(valores))
print("Desvio padrão: ",np.std (valores))
print("80º percentil", np.percentile(valores,80,method="nearest") )
