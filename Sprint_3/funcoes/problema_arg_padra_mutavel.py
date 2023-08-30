#!C:\Users\breno\AppData\Local\Programs\Python\Python311\python.exe
def fibonacci(sequencia=[0,1]):
    #uso de mutáveis como valor default tem uma armadilha
    sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia


if __name__ == '__main__':
    inicio = fibonacci()
    print(inicio, id(inicio))
    print(fibonacci(inicio))
    restart = fibonacci()
    print(restart, id(restart))
    assert restart == [0, 1, 1]