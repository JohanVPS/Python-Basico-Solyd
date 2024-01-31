# nomes =["Guilherme", "Marcelo", "Joao", "Julia"]

# for nome in nomes:
#     print(nome)


# for i in range(len(nomes)):
#     print(nomes[i])
#     nomes.append("OII")

# print(nomes,"\n")

# i=0
# while i<10:
#     print(f"{i} ainda é menor que 10: ")
#     i+=1

qtd = int(input("Qual a quantidade de pessoas serao convidadas para a festa? "))
i = 0
nomes = []
while i<qtd:
    nomes.append(input("Insira o nome da pessoa: "))
    i+=1

print(nomes)