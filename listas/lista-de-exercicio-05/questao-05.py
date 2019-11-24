def SaldoImposto(taxaImposto,custo):
 calculo = taxaImposto/100*custo
 return calculo
 
taxa = int(input("digite sua taxa: "))
custo = int(input("digite o custo: "))
 
a = SaldoImposto(taxa,custo)
print(a)

