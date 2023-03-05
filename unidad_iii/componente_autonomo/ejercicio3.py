# Pide al usuario que ingrese un número entero positivo
numero = int(input("Ingrese un número entero positivo: "))

# Verifica si el número es primo
if numero < 2:  # los números menores que 2 no son primos
    es_primo = False
else:
    es_primo = True
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break

# Imprime el resultado
if es_primo:
    print(f"El número {numero} es primo.")
else:
    print(f"El número {numero} no es primo.")