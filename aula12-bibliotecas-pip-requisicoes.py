import requests

cabecalho = {"User-agent": "Windows 12", "Referer": "https://google.com"}

meuscookies = {"Ultima-visita": "10-10-2020"}

dados = {"username": "Another", "password": "admin"}
texto = None
try:
    requisicao = requests.post("https://putsreq.com/faapdjWbFx7R1nzTpUCO", headers=cabecalho, cookies = meuscookies, data = dados)
    texto = requisicao.text
except Exception as erro:
    print("Requisição deu erro do tipo", erro)

print(texto)
