numero = int(input("digite: "))
def enesimalinha(numero):
    for i in range(1,numero+1):
        print('{} {}'.format(i,'')*i)
        
a = enesimalinha(numero)