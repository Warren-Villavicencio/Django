name = str(input("¿Cuál es tu nombre? "))
edad = int(input("¿Qué edad tienes? "))
altura = float(input("¿Cuál es tu estatura en metros? "))
peso = float(input("¿Cuál es tu peso en kilogramos? "))

print(f"Tu nombre es: {name}, tienes {edad} años, mides {altura} metros y pesas {peso} kg.")

imc = peso / (altura ** 2)
print(f"Tu índice de masa corporal (IMC) es: {imc:.2f}")

if imc < 18.5:
    print("Estás por debajo del peso.")
elif 18.5 <= imc < 25:
    print("Tienes un peso normal.")
elif 25 <= imc < 30:
    print("Tienes sobrepeso.")
else:
    print("Tienes obesidad.")