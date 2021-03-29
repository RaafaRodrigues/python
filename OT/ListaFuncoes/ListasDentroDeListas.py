inventario=[]
resposta= "S"
while resposta == "S":
    equipamento=[
        input("Equipamento: "),
        float(input("Valor: ")),
        int(input("Numero serial: ")),
        input("Departamento: ")
    ]
    inventario.append(equipamento)
    resposta=input("Digite 'S' para continuar: ").upper()

for e in inventario:
    print("Nome: ", e[0])
    print("Valor: ", e[1])
    print("Serial: ", e[2])
    print("Departamento: ",e[3])


busca=input("Digite o nome do equipamento que deseja buscar: ")
for e in inventario:
    if busca.upper() == e[0].upper():
        print("Valor: ", e[1])
        print("Serial: " ,e[2])


depreciacao= input("Digite o nome do equipamento que sera depreciado")
for i in inventario:
    if depreciacao.upper() == i[0].upper():
        print("Valor antigo: ", i[1])
        i[1]= i[1]* 0.9
        print("Valor novo: ",i[1])

serial = int(input("Digite o serial do equipamento que sera excluido"))

for elemento in inventario:
    if serial == elemento[2]:
        inventario.remove(elemento)


for e in inventario:
    print("Nome: ", e[0])
    print("Valor: ", e[1])
    print("Serial: ", e[2])
    print("Departamento: ",e[3])


valores =[]
for elemento in inventario:
    valores.append(elemento[1])
if len(valores) > 0:
    print("O equipamento mais caro custa: ",max(valores))
    print("O equipamento mais barato custa: ", min(valores))
    print("O Total de equipamentos é de: ", sum(valores))
