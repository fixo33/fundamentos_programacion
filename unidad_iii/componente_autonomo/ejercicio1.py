# Define los cargos disponibles
sueldos = ['Ejecutivo', 'Jefe', 'Externo']

# Crea una lista vacía para almacenar los datos de los empleados
empleados = []

# Pide al usuario que ingrese los datos de los empleados
while True:
    c_ident = input("Ingrese el Código de identificación del empleado (o 'salir' para finalizar): ")
    if c_ident == 'salir':
        break
    nombre_apellidos = input("Ingrese el nombre y apellidos del empleado: ")
    cargo = input("Ingrese el cargo del empleado (Ejecutivo, Jefe o Externo): ")

    # Verifica que el cargo ingresado es válido
    if cargo not in sueldos:
        print("El cargo ingresado no es válido.")
        continue

    # Agrega los datos del empleado a la lista
    empleados.append((c_ident, nombre_apellidos, cargo))

# Imprime la lista de empleados con sus sueldos asignados
print("Lista de empleados:")
for empleado in empleados:
    c_ident, nombre_apellidos, cargo = empleado
    sueldo = 0
    if cargo == 'Externo':
        sueldo = 90
    elif cargo == 'Jefe':
        sueldo = 100
    elif cargo == 'Ejecutivo':
        sueldo = 50
    
    # imprime el resultado utilizando cadenas formateadas (f-strings).
    print(f"{c_ident}: {nombre_apellidos} ({cargo}) - Sueldo: ${sueldo}")