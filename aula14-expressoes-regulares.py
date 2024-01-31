import re
import requests

requisicao = requests.get("https://colegiogenesis.com")
padrao = re.findall(r"[\w\.-]+@[\w-]+\.[\w\.-]+", requisicao.text) #RAW String

if padrao:
    print(padrao)
else:
    print("Padrao nao encontrado")