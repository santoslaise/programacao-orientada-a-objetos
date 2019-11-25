def convercao(horas,minutos):

    if(horas>12 and horas<24):
        calculo = horas - 12
        print("{}:{} P.M.".format(calculo,minutos))
    
    elif(horas == 24):
        calculo = horas - 12
        print("{}:{} A.M.".format(calculo,minutos))

    elif(horas == 12):
        calculo = 12
        print("{}:{} P.M.".format(calculo,minutos))

    else:
        print("{}:{} A.M.".format(horas,minutos))


while(True):
    horas = int(input("digite a hora: "))
    minutos = int(input("digite os minutos"))
    convercao(horas,minutos)
    p = input("continuar? ")
    if(p in "não","NÃO","nao","NAO","Nao"):
        break
    else:
        continue