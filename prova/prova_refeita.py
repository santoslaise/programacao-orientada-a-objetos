def convercao(numero):
    calculo = numero/(1024*1024)
    return calculo 
 
#a = convercao(456123789)
#print("{:.2f}".format(a))
 
def calculo_de_percentual(usuario,total):
    percentual = (usuario[2]/total)*100
    usuario.append(percentual)
 
usuarios = []
total = 0
media = 0
 
posicao = 1
with open("usuarios.txt","r") as arquivo:
    for linha in arquivo:
        usuarios.append(linha.split())
 
    for usuario in usuarios:        
        usuario.insert(0,posicao)
        resultado = convercao(float(usuario[2]))
        total += resultado
        usuario[2] = resultado
        posicao += 1
 
       
 
 
    for usuario in usuarios:
        calculo_de_percentual(usuario,total)
 
    media = total/len(usuarios)
 
 
with open("relatorio.txt","w") as arquivo:
    with open("relatorio.txt","w") as dados:
        print(f"ACME Inc.                Uso do espaço em disco pelos usuarios\n{'-'*60}\nNr.        Usuario       Espaço Utilizado      % do uso\n",file=dados)
        for x in range(0, len(usuarios)):
            print('{:<3}     {:<10}      {:>8.2f}MB     {:>6.2f}%'.format(posicao,usuarios[x], convercao(usuario[x]),calculo_de_percentual(usuario[2],total), file=dados)

        print(f'Espaço total ocupado: {total:.2f} MB')
        print(f'Espaço medio ocupado: {media:.2f} MB')
            #print(f'{posicao},   {usuarios},   {convercao(usuario[2]):.2f}\n', file=dados)#
