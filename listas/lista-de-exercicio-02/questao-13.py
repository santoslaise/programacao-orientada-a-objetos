def peso_ideal(usuario,altura):
  if(usuario=="homem"):
    calculo = (72.7*altura)-58
    return calculo
  elif(usuario=="mulher"):
    calc = (62.1*altura)-44.7
    return calc

usuario = input("digite seu sexo: ")
altura = float(input("digite sua altura: "))

a = peso_ideal(usuario,altura)
print("seu peso ideal é: {:.2f}".format(a))