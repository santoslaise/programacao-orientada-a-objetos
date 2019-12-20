class Caneta:
 def __init__(self,cor,marca,numero_ponta,volume_tinta = 50):
   self.cor = cor
   self.marca = marca
   self.numero_ponta = numero_ponta
   self.volume_tinta = volume_tinta
 
 def escrever(self):
   print("sonhos")
   self.volume_tinta-=1
   print(self.volume_tinta)
 
 def encher_caneta(self):
   self.volume_tinta = 50
   print("volume inicial",self.volume_tinta)
 
 def retornar_marca(self):
   return self.marca
 
 
 def imprimir_caracteristicas(self):
   print(f"cor: {self.cor} marca:  {self.marca} numero de ponta: {self.numero_ponta} volume da tinta {self.volume_tinta}")
 
c1 = Caneta("rosa","BIC",2)
c1.escrever()
c1.encher_caneta()
c1.imprimir_caracteristicas()
 
