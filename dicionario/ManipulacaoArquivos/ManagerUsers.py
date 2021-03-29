from Dicionarios.Funcoes import *


usuarios = {}
opcao= perguntar()

while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if(opcao == "I"):
        inserir(usuarios)
    elif(opcao == "E"):
        chave= input("Qual a chave?")
        print(excluirDoArquivo(chave.upper()))
    elif(opcao == "P"):
        chave = input("Qual a chave?")
        print(lerArquivo(chave.upper()))
    elif(opcao == "L"):
        print(listarBd())


    opcao=perguntar()