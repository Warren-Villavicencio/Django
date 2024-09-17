   __             __
       /_ \_.--"""--._/ _\
       \ )   _     _   ( /
        |   (o)___(o)   |
        |      \_/      |
        \       |       /
         \          /
          \_    _    _/
         ___)==( )==(___
       /'      //\      `\
      /       // \\       \
     /   |   |/   \|   |   \
    /,_ /|             |\ _,\
   ((_// |             | \\_))
    `-'  |             |  `-'
         |             |
         |             |
         |      _      |
        /      / \      \
   jgs /      /   \      \
      /      /     \      \
    _/      /       \      \_
   ( _____ /         \ _____ )
    '-----'           `-----'
# validacion_tarjeta.py

def validar_tarjeta(numero_tarjeta):
  """Valida un número de tarjeta de crédito utilizando el algoritmo de Luhn.

  Args:
    numero_tarjeta: El número de tarjeta de crédito como una cadena de caracteres.

  Returns:
    True si el número es válido, False en caso contrario.
  """

  # Convertir el número de tarjeta a una lista de dígitos
  digitos = [int(d) for d in str(numero_tarjeta)]

  # Invertir la lista de dígitos
  digitos.reverse()

  # Multiplicar cada dígito en una posición impar por 2
  for i in range(1, len(digitos), 2):
    digitos[i] *= 2

  # Restar 9 a los dígitos que superen 9
  for i in range(len(digitos)):
    if digitos[i] > 9:
      digitos[i] -= 9

  # Sumar todos los dígitos
  suma = sum(digitos)

  # El número es válido si la suma es divisible por 10
  return suma % 10 == 0

# Programa principal
while True:
  numero_tarjeta = input("Ingrese el número de tarjeta de crédito: ")

  if validar_tarjeta(numero_tarjeta):
    print("El número de tarjeta es válido.")
    break  # Salir del bucle si el número es válido
  else:
    print("El número de tarjeta es inválido. Intente nuevamente.")