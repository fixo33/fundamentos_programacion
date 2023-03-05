def contar_unos_y_ceros(binario):
    """Cuenta la cantidad de unos y ceros en un número binario"""
    unos = 0
    ceros = 0
    for digito in binario:
        if digito == "1":
            unos += 1
        elif digito == "0":
            ceros += 1
    return unos, ceros


# Ejemplo de uso
binario = "11000110101"
unos, ceros = contar_unos_y_ceros(binario)
print(f"El número binario {binario} tiene {unos} unos y {ceros} ceros")
