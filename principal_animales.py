def menu_principal():
    print("--- 🔬 Ejercicio POO: Zoológico Digital (CRUD) 🔬 ---")
    
    # -----------------------------------------------------
    # PRUEBA INICIAL: CREACIÓN (C) DE OBJETOS AUTOMÁTICA
    # -----------------------------------------------------
    print("\n--- Carga Inicial de Ejemplos (Crear) ---")
    
    # Paso 5: Hacer el objeto (implícito en la función crear_animal)
    print(crear_animal(Caballo, "Spirit", 7, "Pradera", "Herbívoro", "Grande", "Marrón"))
    print(crear_animal(Cocodrilo, "Loki", 25, "Río/Pantano", "Carnívoro", "Enorme", "Verde Oscuro"))
    print(crear_animal(Pez, "Nemo", 1, "Océano", "Omnívoro", "Pequeño", "Naranja y Blanco"))
    print(crear_animal(Pato, "Donald", 3, "Estanque", "Omnívoro", "Mediano", "Multicolor"))
    
    # -----------------------------------------------------

    while True:
        print("\n--- MENÚ CRUD ---")
        print("1. [C] Crear un nuevo animal (Agregar)")
        print("2. [R] Leer información detallada de un animal")
        print("3. [R] Listar todos los animales")
        print("4. [U] Actualizar edad de un animal")
        print("5. [D] Eliminar un animal")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            print("\n-- CREAR ANIMAL --")
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            habitat = input("Hábitat: ")
            dieta = input("Dieta: ")
            tamano = input("Tamaño: ")
            color = input("Color: ")
            
            tipo = input("Tipo (Caballo, Cocodrilo, Pez, Escarabajo, Pato): ").capitalize()
            
            clases = {
                "Caballo": Caballo, "Cocodrilo": Cocodrilo, "Pez": Pez, 
                "Escarabajo": Escarabajo, "Pato": Pato
            }
            
            if tipo in clases:
                print(crear_animal(clases[tipo], nombre, edad, habitat, dieta, tamano, color))
            else:
                print("Tipo de animal no válido. Intente de nuevo.")

        elif opcion == '2':
            nombre = input("Ingrese el nombre del animal a leer: ")
            leer_animal(nombre) # Se ejecuta Paso 6 y 7
            
        elif opcion == '3':
            listar_animales()

        elif opcion == '4':
            nombre = input("Ingrese el nombre del animal a actualizar: ")
            try:
                nueva_edad = int(input(f"Nueva edad para {nombre}: "))
                actualizar_animal(nombre, nueva_edad) # Se ejecuta Paso 6
            except ValueError:
                print("Entrada de edad no válida.")
                
        elif opcion == '5':
            nombre = input("Ingrese el nombre del animal a eliminar: ")
            eliminar_animal(nombre)

        elif opcion == '6':
            print("Saliendo del Zoológico Digital. ¡Adiós!")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu_principal()