
inventario = []
resposta:str = "S"
while resposta =="S":
    inventario.append(input("Equipamento: \n"))
    inventario.append(float(input("Valor: \n")))
    inventario.append(int(input("Numero Serial: \n")))
    inventario.append(input("Departamento: \n"))
    resposta=input("Digite \"S\" para continuar: ").upper()
for elemento in inventario:
    print(elemento)