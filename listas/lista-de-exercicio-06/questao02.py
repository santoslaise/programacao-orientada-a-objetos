Questão 02
import random
n_nomes = int(input("digite um numero: "))
 
nome = ["Maria","jõao","Caio","Victor","Emanuelly","Clara","Cristol","Ranny","Lui","Shu","Valt","Max","Engel","Laylla","Lucas","Tayna","Jim","Sara","Bruna","Nara"]
sobrenome = ["silver","Roselly","santos","park","alves","tamires","congelato","flores","luz","pontes","live","Carvalho","Evelyn","Lins","Sasaki","Fay","Gerad","Heroux","Pleassis","simon"]
 
with open("nomes.txt","w") as arquivo:
    for linha in range(0,n_nomes):
        v_nomes = random.randint(0,len(nome)-1)
        v_sobrenomes = random.randint(0,len(sobrenome)-1)
        idade = random.randint(0,90)
        altura = random.uniform(1.50,1.80)
        print("{} {} {} {:.2f}".format(nome[v_nomes],sobrenome[v_sobrenomes],idade,altura), file=arquivo)










