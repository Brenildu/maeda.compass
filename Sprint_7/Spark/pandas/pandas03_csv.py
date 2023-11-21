import pandas as pd

iris = pd.read_csv("./iris.csv")
print(iris)
print("======================")
print(iris[4:10]['sepal_length'])
print("======================")
print("Formato: ", iris.shape)