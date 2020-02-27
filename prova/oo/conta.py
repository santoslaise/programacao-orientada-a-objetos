class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
    def deposita(self,valor):
        self.saldo += valor

    def saca(self, valor):
        #self.saldo-= valor
        if(self.saldo< valor):
            return False
        else:
            self.saldo-= valor
            return True
    def extrato(self):
        print("numero: {} \nsaldo: {}".format(self.numero,self.saldo))

    def transfere_para(self, destino, valor):
        retirar = self.saca(valor)
        if(retirar == false):
            return False
        else:
            destino.deposita(valor)
            return True
