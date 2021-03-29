import platform
from datetime import  datetime
import getpass

#SO
print("Nome maquina: ", platform.node())
print("Arquitetura: ", platform.architecture())
print("Sistema Operacional: ", platform.system())
print("Versão do SO: ", platform.release())
print("Processador: ", platform.processor())
print("Versão do Python", platform.python_version())


#date
print(datetime.now())
print(datetime.now().year)
print(datetime.now().month)
print(datetime.now().day)
print(datetime.now().hour)


#Getpass
usuario = getpass.getuser()
senha = getpass.getpass("Digite sua senha:....")



if usuario == "rafap" and senha == "admin":
    print("Bem vindo ADM")
else:
    print('Você não tem acesso')