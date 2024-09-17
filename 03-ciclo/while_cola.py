# while_cola.py
# Este programa simula una cola de espera utilizando una lista.

cola = []
while True:
    opcion = input("Ingrese una opción (agregar, quitar, mostrar, salir): ")
    if opcion == "agregar":
        elemento = input("Ingrese el elemento a agregar: ")
        cola.append(elemento)
    elif opcion == "quitar":
        if not cola:
            print("La cola está vacía.")
        else:
            print(f"Se quitó: {cola.pop(0)}")
    elif opcion == "mostrar":
        print(cola)
    elif opcion == "salir":
        break
    else:
        print("Opción inválida.")