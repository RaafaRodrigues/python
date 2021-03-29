import socket

resp = "S"
while (resp == "S"):
    url= input("Digite uma url: \n ")
    ip= socket.gethostbyname(url)
    print("O IP referente a url informada é: ",ip)
    resp= input("Digite <S> para continuar: ").upper()