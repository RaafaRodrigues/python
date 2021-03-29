usuarios = {}



usuarios ={
    "chaves":["Chaves do 8", "24/12/2018", "Recep_01"],
    "quico":["Quico das flores", "20/12/2018", "raiox_03"]
}

print(usuarios)

usuarios["florinda"] = ["Dona florinda", "22/12/2018", "Raiox_01"]

print(usuarios)

print(len(usuarios.get("florinda")))
