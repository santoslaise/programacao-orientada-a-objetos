class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
 
    def envelhecer(self):
        self.idade +=1
 
    def engordar(self):
        self.peso+=1
 
    def emagrecer(self):
        self.peso-=2
    def crescer(self):
        if(self.idade<=21):
            self.altura+=0.05
        else:
            return self.altura
 
    def imprimir(self):
        print(f"nome: {self.nome} idade: {self.idade} peso: {self.peso} altura: {self.altura}")
p1 = Pessoa("ana", 19, 50, 1.56)
p1.envelhecer()
p1.engordar()
p1.emagrecer()
p1.crescer()
p1.imprimir()
 
