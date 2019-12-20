class Retangulo:
    def __init__(self,lado_a,lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b
 
    def mudar_valor_lado(self,novo_lado):
        self.lado_a = novo_lado
 
    def retornar_valor_lado(self):
        return self.lado_a
    
    def calcular_area(self):
        calculo = self.lado_a*self.lado_b
        return calculo
 
    def calcular_perimetro(self):
        calc = (2*self.lado_a)+(2*self.lado_b)
        return calc
n1 = int(input("digite um numero: "))
n2 = int(input("degite outro: "))
r1 = Retangulo(n1,n2)
r1.mudar_valor_lado(7)
retorno = r1.retornar_valor_lado()
print("novo lado: ",retorno)
area = r1.calcular_area()
print("area:",area)
perimetro = r1.calcular_perimetro()
print("perimetro: ",perimetro)
 
