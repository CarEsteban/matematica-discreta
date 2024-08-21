# ==========================
# Funciones principales
# ==========================

def main():
    conjuntos = []

    while True:
        mostrar_menu()
        opcion = obtener_opcion()

        # ==========================
        # Opción 1: Construir conjuntos
        # ==========================
        if opcion == 1:
            print("\n--- Opción 1: Construir conjuntos seleccionada ---")
            print("Los conjuntos solo pueden contener letras de la A-Z y números del 0-9.")
            num_conjuntos = obtener_numero_conjuntos()
            
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
                mostrar_conjuntos(conjuntos)
                conjuntoA_idx = obtener_conjunto_para_operar(conjuntos, "primer")
                conjuntoB_idx = obtener_conjunto_para_operar(conjuntos, "segundo")
                print("-----------------------------------------------")
                print(f"Operando entre Conjunto {conjuntoA_idx + 1} como A y Conjunto {conjuntoB_idx + 1} como B")
                print("-----------------------------------------------")
                
                # Mostrar menú de operaciones
                mostrar_menu_operaciones()
                operacion = obtener_opcion_operacion()
                realizar_operacion(operacion, conjuntos[conjuntoA_idx], conjuntos[conjuntoB_idx])
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

def mostrar_menu():
    print("\n========= Menú Principal =========")
    print("1. Construir conjuntos")
    print("2. Operar conjuntos")
    print("3. Finalizar")
    print("==================================")

def obtener_opcion():
    while True:
        try:
            opcion = int(input("Seleccione una opción (1-3): "))
            if opcion in [1, 2, 3]:
                return opcion
            else:
                print("Error: Por favor seleccione una opción válida (1, 2 o 3).")
        except ValueError:
            print("Error: Entrada no válida. Por favor ingrese un número.")

def obtener_numero_conjuntos():
    while True:
        try:
            numero = int(input("¿Cuántos conjuntos desea ingresar?: "))
            if numero > 0:
                return numero
            else:
                print("Error: El número debe ser mayor que cero.")
        except ValueError:
            print("Error: Entrada no válida. Por favor ingrese un número.")

def mostrar_conjuntos(conjuntos):
    print("\nConjuntos disponibles:")
    for idx, conjunto in enumerate(conjuntos):
        print(f"Conjunto {idx+1}: {conjunto}")

def obtener_conjunto_para_operar(conjuntos, orden):
    while True:
        try:
            seleccion = int(input(f"Seleccione el {orden} conjunto para operar (1-{len(conjuntos)}): ")) - 1
            if 0 <= seleccion < len(conjuntos):
                return seleccion
            else:
                print(f"Error: Por favor seleccione un número válido entre 1 y {len(conjuntos)}.")
        except ValueError:
            print("Error: Entrada no válida. Por favor ingrese un número.")

def mostrar_menu_operaciones():
    print("\n========= Menú de Operaciones =========")
    print("1. Complemento")
    print("2. Unión")
    print("3. Intersección")
    print("4. Diferencia")
    print("5. Diferencia Simétrica")
    print("=======================================")

def obtener_opcion_operacion():
    while True:
        try:
            opcion = int(input("Seleccione una operación (1-5): "))
            if opcion in [1, 2, 3, 4, 5]:
                return opcion
            else:
                print("Error: Por favor seleccione una opción válida (1-5).")
        except ValueError:
            print("Error: Entrada no válida. Por favor ingrese un número.")

def realizar_operacion(operacion, conjuntoA, conjuntoB):
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
# Funciones de operaciones con conjuntos (definidas sin implementación)
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
    pass  # Implementar operación de complemento

def realizar_union(conjuntoA, conjuntoB):
    pass  # Implementar operación de unión

def realizar_interseccion(conjuntoA, conjuntoB):
    pass  # Implementar operación de intersección

def realizar_diferencia(conjuntoA, conjuntoB):
    pass  # Implementar operación de diferencia

def realizar_diferencia_simetrica(conjuntoA, conjuntoB):
    pass  # Implementar operación de diferencia simétrica

# ==========================
# Iniciar programa
# ==========================

if __name__ == "__main__":
    main()
