from socket import *

servidor= "127.0.0.1"
porta= 43210

objSocket = socket(AF_INET, SOCK_STREAM)
objSocket.bind((servidor, porta))
objSocket.listen(2)

print("Aguardando cliente...")


while True:
    con, cliente = objSocket.accept()
    print("Conectado com: ", cliente)
    while True:
        mensagemRecebida= str(con.recv(1024))
        print("Recebemos: ", mensagemRecebida)
        mensagemEnviada = b'Ola jovem'
        con.send(mensagemEnviada)
        break
    con.close()