# Lista de frutas
frutas = ["manzana", "pera", "banana"]

def imprimir_fruta(fruta):
    """Imprime el nombre de una fruta en la consola.

    Args:
        fruta (str): El nombre de la fruta a imprimir.
    """
    print(fruta)

# Recorremos la lista de frutas y llamamos a la función para imprimir cada una
for fruta in frutas:
    imprimir_fruta(fruta)