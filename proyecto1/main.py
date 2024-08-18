def mostrar_menu():
    print("Menú Principal")
    print("1. Construir conjuntos")
    print("2. Operar conjuntos")
    print("3. Finalizar")

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

def main():
    while True:
        mostrar_menu()
        opcion = obtener_opcion()

        if opcion == 1:
            print("Opción 1: Construir conjuntos seleccionada.")
            print("Los conjuntos solo pueden contener letras de la A-Z y números del 0-9.")
            elementosA = input("Ingrese los elementos del conjunto A separados por espacios: ")
            conjuntoA = leerConjunto(elementosA)
            elementosB = input("Ingrese los elementos del conjunto B separados por espacios: ")
            conjuntoB = leerConjunto(elementosB)
            print(f"Conjunto A: {conjuntoA}")
            print(f"Conjunto B: {conjuntoB}")
            
        elif opcion == 2:
            print("Opción 2: Operar conjuntos seleccionada.")
            # Aquí iría el código para operar conjuntos
        elif opcion == 3:
            print("Opción 3: Finalizar seleccionada.")
            print("Saliendo del programa...")
            break

#Opciones de operaciones con conjuntos

def leerConjunto(elementos):
    # Verificar que los elementos sean válidos
    conjunto = elementos.split()
    if all(elementos.isalnum and len (elementos) == 1 for elementos in elementos.split()):
        return (conjunto)
    else:
        print("Error: Por favor ingrese elementos válidos.")
        return set()
    

def unirConjuntos(conjuntoA, conjuntoB):
    return {elemento for conjunto in [ conjuntoA, conjuntoB] for elemento in conjunto}

def interseccionConjuntos(conjuntoA, conjuntoB):
    return {elemento for elemento in conjuntoA if elemento in conjuntoB}

def diferenciaConjuntos(conjuntoA, conjuntoB):
    return {elemento for elemento in conjuntoA if elemento not in conjuntoB}

def diferenciaSimetricaConjuntos(conjuntoA, conjuntoB):
    return {elemento for elemento in conjuntoA if elemento not in conjuntoB}.union({elemento for elemento in conjuntoB if elemento not in conjuntoA})


if __name__ == "__main__":
    main()
