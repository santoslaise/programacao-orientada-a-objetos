class Bola:
    def __init__(self,cor,circunferencia,material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
 
    def trocarCor(self,novacor):
        self.cor = novacor
 
    def mostrarCor(self):
        print(self.cor)
 
 
 
b1 = Bola("azul","13","metal")
b1.trocarCor("verde agua")
b1.mostrarCor()
