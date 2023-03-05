def convertir_decimal_a_binario(decimal):
    """Convierte un número decimal a binario"""
    binario = ""
    while decimal > 0:
        resto = decimal % 2
        binario = str(resto) + binario
        decimal = decimal // 2
    return binario


decimal = int(input("Ingrese un número decimal: "))
binario = convertir_decimal_a_binario(decimal)
print(f"El número {decimal} en binario es {binario}")
