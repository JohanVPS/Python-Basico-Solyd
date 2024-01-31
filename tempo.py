import requests
import json

cidade = input("Escreva sua cidade: ")
try:
    requicisao = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + cidade + "&appid=4b141864a907532dd2469e5a289b705d")
except Exception as erro:
    print("Ocorreu um erro do tipo: " + erro)

tempo = json.loads(requicisao.text)
print(tempo["weather"][0]["main"])
print("Temperatura", float(tempo["main"]["temp"]) - 273.15)