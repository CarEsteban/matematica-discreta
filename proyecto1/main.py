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
            # Aquí iría el código para construir conjuntos
        elif opcion == 2:
            print("Opción 2: Operar conjuntos seleccionada.")
            # Aquí iría el código para operar conjuntos
        elif opcion == 3:
            print("Opción 3: Finalizar seleccionada.")
            print("Saliendo del programa...")
            break

if __name__ == "__main__":
    main()
