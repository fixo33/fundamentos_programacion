# Pide al usuario que ingrese un número
numero = int(input("Ingrese un número: "))

# Verifica si el número es par o impar y calcula el cubo o cuadrado, respectivamente
if numero % 2 == 0:  # número es par
    resultado = numero ** 3
    print(f"El número {numero} es par. Su cubo es {resultado}.")
else:  # número es impar
    resultado = numero ** 2
    print(f"El número {numero} es impar. Su cuadrado es {resultado}.")