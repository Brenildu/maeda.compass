#!C:\Users\breno\AppData\Local\Programs\Python\Python311\python.exe
class RGB:
    def __init__(self):
        self.cores = ['red', 'green', 'blue'][::-1]

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return self.cores.pop()
        except IndexError:
            raise StopIteration()
        

if __name__ == '__main__':
    cores = RGB()
    print(next(cores))
    print(next(cores))
    print(next(cores))

    try:
        print(next(cores))
    except StopIteration:
        print('Acabou')

    # é preciso de um objeto interavel e um interetor   
    for cor in RGB():
        print(f'cor: {cor}')