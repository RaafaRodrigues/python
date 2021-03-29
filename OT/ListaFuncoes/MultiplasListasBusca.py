equipamentos=[]
valores=[]
seriais=[]
departamentos=[]
resposta = "S"
while resposta == "S":
    equipamentos.append(input("Equipamento: \n"))
    valores.append(float(input("Valor: \n")))
    seriais.append(int(input("Serial: \n")))
    departamentos.append(input("Departamento: \n"))
    resposta = input("Digite 'S' para continuar:\n ").upper()


buscar = input("\n Digite o nome do equipamento que deseja buscar").upper()
achou = 0

for i in range(0,len(equipamentos)):

    if equipamentos[i].upper() == buscar:
        print("Equipamento ", i+1)
        print("Nome: ", equipamentos[i])
        print("Valor: ", valores[i])
        print("Serial: ",seriais[i])
        print("Departamento: ", departamentos[i])
        achou=achou+1

if achou == 0:
    print("Nenhum equipamento encontrado com esse nome!")
