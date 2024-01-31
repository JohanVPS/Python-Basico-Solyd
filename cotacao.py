import json
import requests

cotacao = None
try:
    requisicao = requests.get("https://api.hgbrasil.com/finance/quotations?key=8d2b1155")
except Exception as erro:
    print("Conexão falhou")
    exit()


resposta = json.loads(requisicao.text)
if resposta["by"] == "default":
    cotacao_compra = resposta["results"]["currencies"]["USD"]["buy"]
    cotacao_venda = resposta["results"]["currencies"]["USD"]["sell"]
    cotacao_variacao = resposta["results"]["currencies"]["USD"]["variation"]

    print("--------------")
    print("A cotação do dolar para compra atualmente é de:", cotacao_compra)
    print("A cotação do dolar para venda atualmente é de:", cotacao_venda)
    print("A variação do dolar atualmente é de:", cotacao_variacao)
    print("--------------")



'''
{"by":"default","valid_key":true,"results":{"currencies":{"source":"BRL","USD":{"name":"Dollar","buy":4.9285,"sell":null,"variation":0.01},
"EUR":{"name":"Euro","buy":5.3735,"sell":null,"variation":0.12},"GBP":{"name":"Pound Sterling","buy":6.2617,"sell":null,"variation":-0.18},
"ARS":{"name":"Argentine Peso","buy":0.006,"sell":null,"variation":-0.03}},"stocks":{"IBOVESPA":{"name":"BM\u0026F BOVESPA","location":"Sao Paulo, Brazil","points":0.0,"variation":0.0},
"NASDAQ":{"name":"NASDAQ Stock Market","location":"New York City, United States","points":0.0,"variation":0.0},
"CAC":{"name":"CAC 40","location":"Paris, French","points":0.0,"variation":0.0},
"NIKKEI":{"name":"Nikkei 225","location":"Tokyo, Japan","points":0.0,"variation":0.0}},"available_sources":["BRL"],
"bitcoin":{"blockchain_info":{"name":"Blockchain.info","format":["USD","en_US"],"last":41660.65,"buy":41660.65,"sell":41660.65,"variation":1.91},
"coinbase":{"name":"Coinbase","format":["USD","en_US"],"last":41663.245,"variation":1.741},"bitstamp":{"name":"BitStamp","format":["USD","en_US"],
"last":41670.0,"buy":41669.0,"sell":41648.0,"variation":1.634},"foxbit":{"name":"FoxBit","format":["BRL","pt_BR"],"last":206935.588,"variation":1.713},
"mercadobitcoin":{"name":"Mercado Bitcoin","format":["BRL","pt_BR"],"last":206606.8,"buy":206606.78824167,"sell":206606.79999999,"variation":1.427}}},
"execution_time":0.0,"from_cache":true}
'''