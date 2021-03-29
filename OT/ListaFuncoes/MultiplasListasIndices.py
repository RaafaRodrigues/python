equipamentos = []
valores = []
seriais = []
departamento = []
resposta = "S"

while resposta == "S":
    equipamentos.append(input("Equipamento: \n"))
    valores.append(float(input("Valor: \n")))
    seriais.append(int(input("Numero serial: \n")))
    departamento.append(input("Departamento: \n"))
    resposta= input("Digite 'S' para continuar: ").upper()

for indice in range(0,len(equipamentos)):
    print("Equipamento: " + str(indice+1))
    print("nome: ", equipamentos[indice])
    print("Valor: ", valores[indice])
    print("Serial: " + str(seriais[indice]))
    print("Departamento: ", departamento[indice])
