def comparar_numeros(num1, num2):
    """Compara dos números y devuelve valores booleanos para diferentes condiciones.

    Args:
        num1 (int): Primer número.
        num2 (int): Segundo número.

    Returns:
        dict: Un diccionario con los resultados de las comparaciones.
    """

    resultados = {
        "iguales": num1 == num2,
        "diferentes": num1 != num2,
        "primero_mayor": num1 > num2,
        "segundo_mayor_igual": num2 >= num1
    }
    return resultados

# Pedimos al usuario que ingrese dos números
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Llamamos a la función para comparar los números y almacenamos los resultados
resultados_comparacion = comparar_numeros(num1, num2)

# Imprimimos los resultados
print("Resultados de la comparación:")
for comparacion, resultado in resultados_comparacion.items():
    print(f"- {comparacion}: {resultado}")

# Pedimos al usuario que ingrese una cadena de texto
cadena = input("Ingrese una cadena de texto: ")

# Comprobamos la longitud de la cadena utilizando operadores lógicos
longitud_valida = len(cadena) >= 4 and len(cadena) <= 7
print(f"La cadena tiene una longitud válida (entre 4 y 7 caracteres): {longitud_valida}")