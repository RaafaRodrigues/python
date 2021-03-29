import json

dicionario = {
    "GODZILLA": ["Exemplo 1", "12/12/2020", "Sala"],
    "KONG": ["Exemplo 2", "13/12/2020", "Sala"],
    "MECHA": ["Exemplo 3", "15/12/2020", "Sala"]
}

print(dicionario)
with open("bd1.json" , "w") as json_file:
    json.dump(dicionario,json_file)

