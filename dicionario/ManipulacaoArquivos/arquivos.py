dados = []

with open("iris.data","r") as arquivo:

    for registro in arquivo.readlines():
        dados.append(registro.split(","))



print(dados)

print(dados[0][0])
print(float(dados[0][0]) + float(dados[0][1]))