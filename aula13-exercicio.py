import requests
import json

def lista_filmes(titulo):
    lista = []
    for i in range(1, 101):
        try:
            req = requests.get("http://www.omdbapi.com/?s=" + titulo + "&type=movie&page="+ str(i) + "&apikey=22ab50d" )
            resposta = json.loads(req.text) #transforma um texto em json e transforma em dicionario       
            if resposta["Response"] == "True":                
                for filme in resposta["Search"]:
                    tit = filme["Title"]
                    ano = filme["Year"]
                    string = tit + " (" + ano + ")"
                    lista.append(string)           
            else:
                break;        
        except:
            print("Erro na conexão")
    return lista

sair = False
while not sair:
    op = input("Pesquise por um filme ou digite SAIR: ")
    if op == "SAIR":
        sair = True    
    else:
        lista_de_filmes = lista_filmes(op)
        print("Filmes encontrados:", len(lista_de_filmes))
        for filme in lista_de_filmes:
            print(filme)      