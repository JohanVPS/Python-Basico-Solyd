import time

def abre_arquivo():
    try:
        open("arquivofic.txt")
        return True
    except Exception as erro:
        print("Aconteceu um erro do tipo:", erro)
        return False
    
while not abre_arquivo():
    print("tentando abrir o arquivo")
    time.sleep(5)

print("Arquivo aberto")