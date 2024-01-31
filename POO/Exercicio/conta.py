
class Conta:
    def __init__(self, cliente):
        self.cliente = cliente
        self.saldo = 0
        self.limite = 4

    def deposito(self, qtdDeposito):
        if qtdDeposito > 0:
            self.saldo += qtdDeposito
        else: 
            print("Você é maluco!!!!!!")    

    def saque(self, qtdSaque):
        if qtdSaque > 0 and qtdSaque <= self.saldo:
            self.saldo -= qtdSaque
        else:
            print("Voce não pode sacar esse valor, ou o valor de saque é inferior ao permitido ou você esqueceu que é pobre e quis sacar mais do que tem")

    def consultaSaldo(self):
        return self.saldo

