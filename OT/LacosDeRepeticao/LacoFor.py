tabuada:int =int(input("Digite um numero para exibir a tabuada: \n"))

print("Tabuada do numero " ,tabuada)
for valor in range(0,10,1):
    print(str(tabuada) + " x " + str(valor+1) + " = "+ str((tabuada*(valor+1))))
