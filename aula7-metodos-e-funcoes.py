import sys
sys.path.append("D:/Coringuei/Programação/Language_Python")
from Header import basics

def numMaior(argumento):
    maior = max(argumento)
    return maior

colecao = {1,4,21,6345,7.9,343}
maior = numMaior(colecao)
print(maior)