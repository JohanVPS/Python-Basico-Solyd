from cliente import Cliente
from conta import Conta

cliente1 = Cliente("sla", "123.456.789-10", 19)


conta1 = Conta(cliente1, 10.50, 1000)

print(conta1.cliente.nome, conta1.consulta_saldo())

conta1.depositar(1000.40)

print(conta1.consulta_saldo())

conta1.sacar(500)

print(conta1.consulta_saldo())

conta1.sacar(1000)

print(conta1.consulta_saldo())