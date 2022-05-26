class Cliente:
    def __init__(self, nome, sexo, idade):
        self.nome = nome
        self.sexo = sexo
        self.idade = idade

    def comprar(self):
        print(f'{self.nome} está comprando')
        
        
    
class Produto:
    def eletronico(self, televisao, notebook):
        self.televisao = televisao
        self.notebook = notebook
        print(f'{self.nome} está comprando uma {self.televisao}')    
    
 
