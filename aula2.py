import os

nome = str(input("Qual seu nome: ").capitalize())
cpf = str(input("Qual seu cpf: "))
endereco = str(input("Qual seu endereco: "))
idade = int(input("Qual seu idade: "))
altura = float(input("Qual seu altura: "))
telefone = str(input("Qual seu telefone: "))

os.system('cls')
print("\n\nRelatório".upper())
print("Nome: ", nome, "\ncpf: ", cpf, "\nendereco: ", endereco, "\nIdade: ", idade, "\nAltura: ", altura, "\nTelefone", telefone)