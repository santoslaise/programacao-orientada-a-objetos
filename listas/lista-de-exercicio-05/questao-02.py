numero = int(input("numero: "))
 
def enesima(numero):
 lista = []
 while numero not in lista:
   for numero in range(1,numero+1):
     lista.append(numero)
     a = str(lista).strip("[]").replace(','," ")
     print(a)
     
enesima(numero)
