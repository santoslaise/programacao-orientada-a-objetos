class Computador:
    def __init__(self, marca, modelo, componentes, anos_uso, cor):
        self.marca = marca
        self.modelo = modelo
        self.componentes = componentes
        self.anos_uso = anos_uso
        self.cor = cor
 
 
    def mostrarMarca(self):
        print(self.marca)
 
    def adicionarComponentes(self,novo_componentes):
        self.componentes.append(novo_componentes)
 
    def mostrarComponentes(self):
        print(self.componentes)
 
    def mostrar_anos_uso(self):
        if(self.anos_uso<6):
            print(self.anos_uso)
        elif(self.anos_uso>=6):
            print( "Seu computador está tão velho que tem problemas de junta… junta tudo e joga fora...")
        
 
    def envelhecer(self):
        self.anos_uso+=1
    
 
 
c1 = Computador("cce","padrão",["teclado","monitor"],15 ,"preto")
c1.adicionarComponentes("mouse")
c1.mostrarMarca()
c1.mostrarComponentes()
c1.mostrar_anos_uso()
c1.envelhecer()