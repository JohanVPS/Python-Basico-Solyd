class Conta:

    def __init__(self, cliente, saldo, limite):
        self.cliente = cliente
        self.saldo = saldo
        self.limite = 0 - limite

    def __str__(self):
        return "Nome: " + self.nome + "\nCPF: " + self.cpf + "\nIdade: " + str(self.idade) + "Saldo: " + str(self.saldo)
    
    def depositar(self, quant):
        if quant > 0:
            self.saldo += quant
            print("Depósito de:", quant, "realizado com sucesso")
        else:
            print("Erro no depósito")

    def consulta_saldo(self):
        return str(self.saldo)
    
    def sacar(self, quant):
        if self.saldo - quant < self.limite:
            print("Saldo insuficiente")
        else:
            self.saldo -= quant
            print("Saque de:", quant, "realizado com sucesso")