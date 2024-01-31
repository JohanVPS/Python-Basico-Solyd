from veiculo import Veiculo

class Carro(Veiculo):

    def __init__(self, cor, marca, tanque):
        super().__init__(cor, 4, marca, tanque)
    def abastecer(self, litros):
        if self.tanque + litros > 50:
            print("Tanque com, capacidade inferior")
        else:
            return super().abastecer(litros)
