import serial
from serial.tools import list_ports

for port in list_ports.comports():
    print("Dispositivo: {} - porta: {} ".format(port.description,port.device))



conexao = serial.Serial("COM3",115200)

acao = input("Digite \n<L> para Ligar \n <D> para desligar").upper()

while acao == "L" or acao == "D":
    if(acao == "L"):
        conexao.write(b'1')
    else:
        conexao.write(b'0')

    acao = input("Digite \n<L> para Ligar \n <D> para desligar").upper()

conexao.close()
print("Conexão encerrada")