from Dicionarios.Funcoes import *

usuarios = {}
opcao = perguntar()

while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao == "I":
        inserir(usuarios)
    elif opcao == "P":
        chave = input("Chave do usuario:").upper()
        print(pesquisar(usuarios,chave))

    elif opcao == "E":
        print(exluir(usuarios,input("Chave do usuario:").upper()))

    elif opcao == "L":
        print(listar(usuarios))

    else:
        break

    opcao = perguntar()
