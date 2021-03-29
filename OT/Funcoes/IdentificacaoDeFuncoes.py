

def preencherInventario(lista):
    resposta = "S"
    while resposta == "S":
        equipamento=[
        input("Equipamento: "),
        float(input("Valor: ")),
        int(input("Numero serial: ")),
        input("Departamento: ")
        ]
        lista.append(equipamento)
        resposta=input("Digite 'S' para continuar: ").upper()

def exibirInventario(lista):
    for e in lista:
        print("Nome: ", e[0])
        print("Valor: ", e[1])
        print("Serial: ", e[2])
        print("Departamento: ",e[3])

def localizarPorNome(lista):
    busca=input("Digite o nome do equipamento que deseja buscar: ")
    for e in lista:
        if busca.upper() == e[0].upper():

            print("Valor: ", e[1])
            print("Serial: " ,e[2])


def depreciarPorNome(lista,porcentagem):
    depreciacao= input("Digite o nome do equipamento que sera depreciado")
    for i in lista:
        if depreciacao.upper() == i[0].upper():

            print("Valor antigo: ", i[1])
            i[1]= i[1] * porcentagem
            print("Valor novo: ",i[1])


def excluirPorSerial(lista):

    serial = int(input("Digite o serial do equipamento que sera excluido"))

    for elemento in lista:
        if serial == elemento[2]:
            lista.remove(elemento)
            return "Item exluido"

    return "item nao encontrado"

def exibirValores(lista):

    valores =[]
    for elemento in lista:
        valores.append(elemento[1])

    if len(valores) > 0:

        print("O equipamento mais caro custa: ",max(valores))
        print("O equipamento mais barato custa: ", min(valores))
        print("O Total de equipamentos é de: ", sum(valores))
