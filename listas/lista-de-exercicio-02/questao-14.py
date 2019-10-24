peso = float(input("digite o peso: "))
if(peso>50):
  calculo = (peso - 50)
  multa = calculo*4
  print("exesso do limite de {:.2f} multa de:{:.2f}".format(calculo,multa))
else:
  print("esta dentro do limite")