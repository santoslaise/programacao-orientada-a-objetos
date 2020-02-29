from datetime import datetime
class Conta:
    def __init__(self, numero, titular, saldo, limite,data_abertura):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.data_abertura = data_abertura
        self.historico = Historico()
        
    def deposita(self,valor):
        self.saldo += valor
        self.historico.transacoes.append(f"depósito de {valor}")

    def saca(self, valor):
        #self.saldo-= valor
        if(self.saldo< valor):
            return False
        else:
            self.saldo-= valor
            self.historico.transacoes.append(f"saque de {valor}")

            #return True
    def extrato(self,dados_cliente):
        print("\nExtrato da conta do cliente:\ndata de abertura: {}\n{}\nnumero da conta: {} \nsaldo: {}".format(self.data_abertura, dados_cliente,self.numero,self.saldo))
        self.historico.transacoes.append(f"extrato - saldo de:{self.saldo}") 


    def transfere_para(self, destino, valor):
        retirar = self.saca(valor)
        if(retirar == False):
            return False
        else:
            destino.deposita(valor)
            self.historico.transacoes.append(f"trasferencia de{valor} para conta de {destino.numero}") 

            



class Cliente:
    def __init__(self,nome,sobrenome,cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def __str__(self):
        return (f"nome: {self.nome}\nsobrenome: {self.sobrenome}\nCPF: {self.cpf}")


class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        return("{}/{}/{}".format(self.dia,self.mes,self.ano))

class Historico:
    def __init__(self):
        self.data_abertura = datetime.today()
        self.transacoes = []
        
    def imprimir(self):
        print(f"data em que foi aberta a conta: {self.data_abertura}")
        print(f"transações:")
        for i in self.transacoes:
            print("-", i)
        
        

            
def main():
    cliente1 = Cliente('joao','alves','777777-9')
    cliente2 = Cliente('luiza', "rose'", "112233-4")
    data = Data('20','02','2020')
    conta = Conta('123-4', cliente1.nome, 120.0,1000.0,data)
    conta02 = Conta('142-4', cliente2, 102,5000.0,data)
    conta.deposita(30)
    conta.saca(50)
    conta.transfere_para(conta02,23)
    conta.extrato(cliente1)
    conta.extrato(cliente2)
    conta.historico.imprimir()
    conta02.historico.imprimir()
    
       
if __name__=='__main__':
    main()

 

