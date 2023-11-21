import pandas as pd
import numpy as np

arquivo = pd.read_csv('./actors')

nomes = arquivo['Actor'].upper()

print(nomes)