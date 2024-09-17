# while_factorial.py
# Este programa calcula el factorial de un número ingresado por el usuario.

numero = int(input("Ingrese un número: "))
factorial = 1
i = 1
while i <= numero:
    factorial *= i
    i += 1

print(f"El factorial de {numero} es: {factorial}")