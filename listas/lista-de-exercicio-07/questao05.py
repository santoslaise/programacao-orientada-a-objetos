class Pokemon:
    def __init__(self,nome, tipo, descricao, ataques, nivel, poder_luta, brilhante=True):
        self.nome = nome
        self.tipo = tipo
        self.descricao = descricao 
        self.ataques = ataques 
        self.nivel = nivel 
        self.poder_luta = poder_luta
        self.brilhante = brilhante 
 
    
    def adicionar_ataque(self,ataque):
        self.ataques.append(ataque)
 
    def mostrar_ataques(self):
 
         print(self.ataques)
  
 
    def subir_nivel(self):
        self.nivel +=1
        print("nivel: ",self.nivel)
 
 
    def mostrar_poder_luta(self):
        print("poder de luta",self.poder_luta)
 
    def e_brilhante(self):
        if(self.brilhante ==True):
            print("***é brilhante***")
        else:
            print("###nao é brilhante!###")
    def imprimir(self):
        print(f"**pokemon**\nnome: {self.nome}\ntipo: {self.tipo}\ndescrição: {self.descricao}")
 
 
p1 = Pokemon("luz"," raio solar","viaja na velocidade da luz", [], 2,"95")
p1.adicionar_ataque("ataque de fogo")
p1.imprimir()
p1.mostrar_ataques()
p1.subir_nivel()
p1.mostrar_poder_luta()
p1.e_brilhante()
