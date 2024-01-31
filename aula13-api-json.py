import requests
import json

def requisicao(titulo):
    try:
        req = requests.get("http://www.omdbapi.com/?t=" + titulo + "&apikey=22ab50d")
        dicionario = json.loads(req.text) #transforma um texto em json e transforma em dicionario
        return dicionario
    except:
        print("Erro na conexão")
        return None
    
def printar_detalhes(filme):
    print("Titulo:", filme['Title'])
    print("Ano:", filme['Year'])
    print("Diretor:", filme['Director'])
    print("Atores", filme['Actors'])
    print("Nota:", filme['imdbRating'])
    print("Premios", filme['Awards'])
    print("Poster", filme['Poster'])
    print("-----------------------")

sair = False
while not sair:
    op = input("Escreva o nome de um filme ou SAIR para fechar: ")
    if op == "SAIR":
        sair = True
    else:
        filme = requisicao(op)
        if filme["Response"] == "False":
            print("Filme não encontrado")
        else:
            printar_detalhes(filme)    
