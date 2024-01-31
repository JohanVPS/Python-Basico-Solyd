from random import sample
from conta import Conta
class Cliente:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.saldo = 0
        self.limite = 4
        
