def menu():
    while True:
        print("\n--- Menú del Sistema ---")
        print("1. Inicializar Sistema. ")
        print("2. Crear catalogo de experimentos. ")
        print("3. Desarrollar un experimento. ")
        print("4. Mostrar datos del Estudiante. ")
        print("5. SALIR")
        opcion = int(input("Ingrese un valor. "))

        if opcion == 1 :
            print("\nInicializando el sistema.")
        elif opcion == 2 :
            print("\nCreando Catalogo de Experimentos.")
        elif opcion == 3 :
            print("\nDesarrollando un experimento. ")
        elif opcion == 4 :
            print("\nDatos del Estudiante: ")
            print(" Nombre:Hugo Lizandro Ramirez Siquinajay. ")
            print(" Carnet: 201800956. ")
        elif opcion == 5:
            print ("\nGracias por utilizar el sistema. \nHasta luego \nVuelva pronto.")
            break
        else:
            print("Opcion incorrecta, ingrese una opcion valida")

print("-------------------")
menu()
print("-------------------")