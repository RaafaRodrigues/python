nome=input("Digite seu nome: ")
idade=int(input("Digite sua idade: "))

if idade >=65:
    print("O paciente " + nome +" Possui atendimento prioritario")
else:
    print("O paciente " + nome + " Não possui atendimento prioritario")