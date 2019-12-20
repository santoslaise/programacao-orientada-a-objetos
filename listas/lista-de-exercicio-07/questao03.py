 
class Quadrado:
    def __init__(self,tamanho_lado):
        self.tamanho_lado = tamanho_lado
    
 
    def mudar_valor_lado(self,novo_valor):
        self.tamanho_lado = novo_valor
 
    def retornar_valor_lado(self):
        return self.tamanho_lado
 
    def calcular_area(self):
        calculo = self.tamanho_lado*self.tamanho_lado
        return calculo
 
q1 = Quadrado(17)
q1.mudar_valor_lado(26)
lado = q1.retornar_valor_lado()
print(lado)
area = q1.calcular_area()
print(area)