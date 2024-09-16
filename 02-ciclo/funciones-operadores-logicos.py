def obtener_valores():
    while True:
        try:
            valor_uno = float(input("Ingresa el primer valor: "))
            valor_dos = float(input("Ingresa el segundo valor: "))
            return valor_uno, valor_dos
        except ValueError:
            print("Por favor, ingresa valores numéricos válidos.")

def comparar_valores(valor_uno, valor_dos):
    print("¿El primer valor es menor o igual al segundo?", valor_uno <= valor_dos)
    print("¿Los valores son diferentes?", valor_uno != valor_dos)
    print("¿Los valores son iguales?", valor_uno == valor_dos)

def operadores_logicos(valor_uno, valor_dos):
    print("Resultado del operador OR:", valor_uno or valor_dos)
    print("Resultado del operador AND:", valor_uno and valor_dos)

# Comparaciones
valor_uno, valor_dos = obtener_valores()
comparar_valores(valor_uno, valor_dos)

# Operadores lógicos
valor_uno, valor_dos = obtener_valores()
operadores_logicos(valor_uno, valor_dos)
