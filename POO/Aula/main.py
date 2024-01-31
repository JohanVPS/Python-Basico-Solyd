from veiculo import Veiculo
from carro import Carro

caminhao_rosa = Veiculo("rosa", 6, "ford", 30)

print(caminhao_rosa.cor, caminhao_rosa.rodas, caminhao_rosa.marca, caminhao_rosa.tanque)
caminhao_rosa.abastecer(20)
print(caminhao_rosa.tanque)

carro_azul = Carro("azul", "nissan", 30)
print(carro_azul.tanque)
carro_azul.abastecer(10)
print(carro_azul.tanque) 