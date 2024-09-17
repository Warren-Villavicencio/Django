

#logicos

edad = int(input("Ingresa tu edad ")) 
cedula = str(input("Tienes cédula de identidad si o no ")) 
if edad >= 18 and edad <= 35 and cedula == "si":
    print("puedes ingresar")
else:
    print("no puedes ingresar")


