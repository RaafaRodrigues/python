import json

with open("bd.json","r") as arqJson:
    dic= json.load(arqJson)
    for chave,dados in dic.items():
        print(chave + " " + str(dados))




