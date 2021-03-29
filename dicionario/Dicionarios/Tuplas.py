usuarios = {}
emails = ["rafa@email.com", "email@rafa.com"]

tupla = list(enumerate(emails))

for chave in range(0, len(tupla)):
    print("Email: ", tupla[chave][1])
    usuarios[tupla[chave]] = [input("Digite o nome: \n"), input("Digite o nivel\n")]

for chave, dado in usuarios.items():
    print("\nUsuario: ", chave[0])
    print("Email: ", chave[1])
    print("Nome: ", dado[0])
    print("Nivel: ", dado[1])
