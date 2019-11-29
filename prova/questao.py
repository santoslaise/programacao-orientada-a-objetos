
#a = open("usuarios.txt","r")
#with open("relatorio.txt","w") as arquivo:
 #   for linha in arquivo:
  #      print(linha),file=arquivo





def conversao(bits):
    calculo = (-8000000+bits)
    c = calculo-2581,57
    return(c)

a = conversao(456123789)
print("{:.2f}".format(a))



#def percentual(espaco_total,valor_inicial):
 #   calculo = (espaco_total/valor_inicial)*100
  #  multiplicacao = calculo-100
   # return multiplicacao

#a = percentual(3011.83,456123789)
#print("{:.2f}".format(a))

    

