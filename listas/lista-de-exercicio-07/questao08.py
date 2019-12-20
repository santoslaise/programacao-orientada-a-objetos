class Tamagotchi:
    def __init__(self,nome, fome=10,saude=10,idade=0):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
 
    def alterar_nome(self,novo_nome):
        self.nome = novo_nome
    
    def retornar_fome(self):
        return self.fome
    def retornar_saude(self):
        return self.saude
    def retornar_idade(self):
        return self.idade
    def comer(self):
        self.fome+=1
    def tomar_injecao (self):
        self.saude+=1
    def envelhecer (self):
        self.idade-=1
        self.saude-=1
        self.idade+=3
 
    def imprimir (self):
        print(f"nome: {self.nome} fome: {self.fome} saude: {self.saude} idade: {self.idade}")
 
t1 = Tamagotchi("util")
t1.alterar_nome("electro")
t1.retornar_fome()
t1.retornar_saude()
t1.retornar_idade()
t1.comer()
t1.tomar_injecao()
t1.envelhecer()
t1.imprimir()
