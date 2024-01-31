from cliente import Cliente
from conta import Conta
import time
import os

listaCliente = []
listaConta = []
op = "" 
encontrou = False

while op != 5:
 
    op = int(input("1.Cadastrar cliente e criar sua conta\n2.Sacar\n3.Depositar\n4.Consultar saldo\n5.Sair\n\n->"))


    if op == 1:

        nomeCliente = input("Qual o nome do cliente?\n->")
        cpfCliente = input("Qual o cpf do cliente?\n->")
        idadeCliente = int(input("Qual a idade do cliente?\n->"))

        cliente = Cliente(nomeCliente, cpfCliente, idadeCliente)
        conta = Conta(cliente.nome)
        
        lista = {cliente:conta}


        listaCliente.append(cliente)
        listaConta.append(conta)


        #percorre e mostrar o que foi salvo dentro da lista
        # for cliente in listaCliente:
        #     print(cliente.nome)
            
        
    
    elif op == 2:
        buscaNome = input("Quem deseja sacar?\n->")
        
        for cliente in listaCliente:
            if buscaNome == cliente.nome:
                encontrou = True
                break

        if encontrou == False:
            print("Cliente não encontrado")
        else:
            qtdSaque = float(input("Qual o valor do saque?\n->"))
            if qtdSaque > 0 and qtdSaque <= cliente.saldo:
                cliente.saldo -= qtdSaque
            else:
                print("Voce não pode sacar esse valor, ou o valor de saque é inferior ao permitido ou você esqueceu que é pobre e quis sacar mais do que tem")



    elif op == 3:
        buscaNome = input("Quem deseja depositar?\n->")
        
        for cliente in listaCliente:
            if buscaNome == cliente.nome:
                encontrou = True
                break

        if encontrou == False:
            print("Cliente não encontrado")
        else:
            qtdDeposito = float(input("Qual o valor do depósito?\n->"))
            if qtdDeposito > 0:
                cliente.saldo += qtdDeposito
            else: 
                print("Você é maluco!!!!!!")
    
    elif op == 4:
        buscaNome = input("De quem é o saldo que quer consultar?\n->")
        
        for cliente in listaCliente:
            if buscaNome == cliente.nome:
                print(conta.saldo)
                encontrou = True
                break

        if encontrou == False:
            print("Cliente não encontrado")
    
    elif op == 5:
        break

    else:
        print("Por favor, insira uma opção válida!")
        time.sleep(2)

    #os.system("cls")