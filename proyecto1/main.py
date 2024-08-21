# ==========================
# Proyecto 1: Matematica Discreta
# Integrante 1: Nicolás Concuá - 23197
# Integrante 2: Esteban Carcamo - 23016
# Operación de Conjuntos
# ==========================


# ==========================
# Funciones principales
# ==========================

def main():
    conjuntos = []

    while True:
        mostrarMenu()
        opcion = obtenerOpcion()

        # ==========================
        # Opción 1: Construir conjuntos
        # ==========================
        if opcion == 1:
            print("\n--- Opción 1: Construir conjuntos seleccionada ---")
            print("Los conjuntos solo pueden contener letras de la A-Z y números del 0-9.")
            num_conjuntos = obtenerNumConjuntos()
            
            for i in range(len(conjuntos), len(conjuntos) + num_conjuntos):
                elementos = input(f"Ingrese los elementos del conjunto {i+1} separados por espacios: ")
                conjunto = leerConjunto(elementos)
                conjuntos.append(conjunto)
                print(f"Conjunto {i+1}: {conjunto}")
            print("-----------------------------------------------\n")

        # ==========================
        # Opción 2: Operar conjuntos
        # ==========================
        elif opcion == 2:
            if len(conjuntos) == 0:
                print("\nError: Por favor ingrese conjuntos primero.")
            elif len(conjuntos) == 1:
                print("\nError: Hace falta un conjunto más para operar.")
            else:
                print("\n--- Opción 2: Operar conjuntos seleccionada ---")
                mostarConjuntos(conjuntos)
                conjuntoA_idx = obtenerConjuntoParaOperar(conjuntos, "primer")
                conjuntoB_idx = obtenerConjuntoParaOperar(conjuntos, "segundo")
                print("-----------------------------------------------")
                print(f"Operando entre Conjunto {conjuntoA_idx + 1} como A y Conjunto {conjuntoB_idx + 1} como B")
                print("-----------------------------------------------")
                
                # Mostrar menú de operaciones
                menuOperaciones()
                operacion = opcionDeOperacion()
                realizarOperacion(operacion, conjuntos[conjuntoA_idx], conjuntos[conjuntoB_idx])
                print("-----------------------------------------------\n")
        
        # ==========================
        # Opción 3: Finalizar programa
        # ==========================
        elif opcion == 3:
            print("\n--- Opción 3: Finalizar seleccionada ---")
            print("Saliendo del programa...")
            print("---------------------------------------")
            break

# ==========================
# Funciones auxiliares
# ==========================

def mostrarMenu():
    print("\n========= Menú Principal =========")
    print("1. Construir conjuntos")
    print("2. Operar conjuntos")
    print("3. Finalizar")
    print("==================================")

def obtenerOpcion():
    while True:
        try:
            opcion = int(input("Seleccione una opción (1-3): "))
            if opcion in [1, 2, 3]:
                return opcion
            else:
                print("Error: Por favor seleccione una opción válida (1, 2 o 3).")
        except ValueError:
            print("Error: Entrada no válida. Por favor ingrese un número.")

def obtenerNumConjuntos():
    while True:
        try:
            numero = int(input("¿Cuántos conjuntos desea ingresar?: "))
            if numero > 0:
                return numero
            else:
                print("Error: El número debe ser mayor que cero.")
        except ValueError:
            print("Error: Entrada no válida. Por favor ingrese un número.")

def mostarConjuntos(conjuntos):
    print("\nConjuntos disponibles:")
    for idx, conjunto in enumerate(conjuntos):
        print(f"Conjunto {idx+1}: {conjunto}")

def obtenerConjuntoParaOperar(conjuntos, orden):
    while True:
        try:
            seleccion = int(input(f"Seleccione el {orden} conjunto para operar (1-{len(conjuntos)}): ")) - 1
            if 0 <= seleccion < len(conjuntos):
                return seleccion
            else:
                print(f"Error: Por favor seleccione un número válido entre 1 y {len(conjuntos)}.")
        except ValueError:
            print("Error: Entrada no válida. Por favor ingrese un número.")

def menuOperaciones():
    print("\n========= Menú de Operaciones =========")
    print("1. Complemento")
    print("2. Unión")
    print("3. Intersección")
    print("4. Diferencia")
    print("5. Diferencia Simétrica")
    print("=======================================")

def opcionDeOperacion():
    while True:
        try:
            opcion = int(input("Seleccione una operación (1-5): "))
            if opcion in [1, 2, 3, 4, 5]:
                return opcion
            else:
                print("Error: Por favor seleccione una opción válida (1-5).")
        except ValueError:
            print("Error: Entrada no válida. Por favor ingrese un número.")

def realizarOperacion(operacion, conjuntoA, conjuntoB):
    if operacion == 1:
        realizar_complemento(conjuntoA, conjuntoB)
    elif operacion == 2:
        realizar_union(conjuntoA, conjuntoB)
    elif operacion == 3:
        realizar_interseccion(conjuntoA, conjuntoB)
    elif operacion == 4:
        realizar_diferencia(conjuntoA, conjuntoB)
    elif operacion == 5:
        realizar_diferencia_simetrica(conjuntoA, conjuntoB)

# ==========================
# Funciones de operaciones con conjuntos 
# ==========================

def leerConjunto(elementos):
    # Verificar que los elementos sean válidos y no repetidos
    conjunto = set()
    for elemento in elementos.split():
        if elemento.isalnum() and len(elemento) == 1:
            conjunto.add(elemento)  # Añadir elemento al conjunto, evitando duplicados
        else:
            print(f"Error: '{elemento}' no es un elemento válido.")
    return conjunto

def realizar_complemento(conjuntoA, conjuntoB):
    # El complemento de A en B (elementos en B que no están en A)
    complementoA = [elemento for elemento in conjuntoB if elemento not in conjuntoA]
    complementoB = [elemento for elemento in conjuntoA if elemento not in conjuntoB]
    print(f"Complemento de A respecto a B: {complementoA}")
    print(f"Complemento de B respecto a A: {complementoB}")

def realizar_union(conjuntoA, conjuntoB):
    # La unión de A y B (elementos que están en A o en B, sin duplicados)
    union = list(conjuntoA)  # Convertimos el conjunto a una lista para poder usar append
    for elemento in conjuntoB:
        if elemento not in union:
            union.append(elemento)
    print(f"Unión de A y B: {union}")

def realizar_interseccion(conjuntoA, conjuntoB):
    # La intersección de A y B (elementos que están en ambos conjuntos)
    interseccion = [elemento for elemento in conjuntoA if elemento in conjuntoB]
    print(f"Intersección de A y B: {interseccion}")

def realizar_diferencia(conjuntoA, conjuntoB):
    # La diferencia de A y B (elementos que están en A pero no en B)
    diferencia = [elemento for elemento in conjuntoA if elemento not in conjuntoB]
    print(f"Diferencia de A menos B: {diferencia}")

def realizar_diferencia_simetrica(conjuntoA, conjuntoB):
    # La diferencia simétrica de A y B (elementos que están en A o en B pero no en ambos)
    diferencia_simetrica = []
    for elemento in conjuntoA:
        if elemento not in conjuntoB:
            diferencia_simetrica.append(elemento)
    for elemento in conjuntoB:
        if elemento not in conjuntoA:
            diferencia_simetrica.append(elemento)
    print(f"Diferencia Simétrica de A y B: {diferencia_simetrica}")

# ==========================
# Iniciar programa
# ==========================

main()
