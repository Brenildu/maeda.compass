# Crie uma classe chamada Pessoa, com um atributo privado chamado nome (declarado internamente na classe como __nome) e 
# um atributo público de nome id.

#Adicione dois métodos à classe, sendo um para definir o valor de __nome e outro para retornar o valor do respectivo atributo.

#Lembre-se que o acesso ao atributo privado deve ocorrer somente através dos métodos definidos, nunca diretamente.  
# Você pode alcançar este comportamento através do recurso de properties do Python.

# Veja um exemplo de como seu atributo privado pode ser lido e escrito:

# pessoa = Pessoa(0) 
# pessoa.nome = 'Fulano De Tal'
# print(pessoa.nome)

class Ordenadora:
    def __init__(self, listaBaguncada):
        self.listaBaguncada = listaBaguncada
    
    def ordenacaoCrescente(self):
        return sorted(self.listaBaguncada)
    
    def ordenacaoDecrescente(self):
        return sorted(self.listaBaguncada, reverse=True)

# Instanciando objetos com listas baguncadas
crescente = Ordenadora([3, 4, 2, 1, 5])
decrescente = Ordenadora([9, 7, 6, 8])

# Imprimindo resultados da ordenação
print(crescente.ordenacaoCrescente())
print(decrescente.ordenacaoDecrescente())