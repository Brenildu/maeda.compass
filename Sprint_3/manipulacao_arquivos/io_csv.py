#!C:\Users\breno\AppData\Local\Programs\Python\Python311\python.exe

import csv

with open('pessoas.csv') as entrada:
    for pessoa in csv.reader(entrada):
        print('Nome: {}, Idade: {}'.format(*pessoa))