import serial
from serial.tools import list_ports

conexao = ""
for port  in list_ports.comports():
    print("Dispositivo: {} - porta {}".format(port.description,port.device))
    if("ARDUINO" in port.description.upper()):
        try:
            conexao = serial.Serial(port.device,115200)
            print("Conexão realizada com {}".format(conexao.portstr))
        except:
            pass

if(conexao != ""):
    while True:
        resposta=conexao.readline()
        valor = float(resposta.decode())
        print(valor)
        if(valor < 700 ):
            conexao.write(b'1')
        else:
            conexao.write(b'0')

    conexao.close()
    print("Conexão encerrada")
else:
    print("Sem portas disponiveis")