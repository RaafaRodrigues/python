nome=input("Digite seu nome: \n")
idade=int(input("Digite sua idade: \n"))
doencaInfectocontagiosa=input("Suspeita de doença Infectocontagiosa? \n").upper()
if idade >= 65:
    print("O paciente " + nome + "POSSUI atendimento prioritario")
elif doencaInfectocontagiosa.upper() =="SIM":
    print("O paciente " + nome + " deve ser direcionado para a sala de espera reservada.")
else:
    print("O paciente " + nome + " NÃO possui atendimento prioritario e pode aguardadr na sala comum!")

