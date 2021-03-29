from socket import *

servidor = "127.0.0.1"
porta = 43210

msg = bytes(input("Digite algo: "),"utf-8")
objSocket = socket(AF_INET, SOCK_STREAM)
objSocket.connect((servidor, porta))
objSocket.send(msg)

resposta = objSocket.recv(1024)
print("Recebemos: ",resposta)
objSocket.close()