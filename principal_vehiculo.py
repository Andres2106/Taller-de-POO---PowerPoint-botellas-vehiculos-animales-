from Vehiculo_caro import VehiculoCaro
from Vehiculo_barato import VehiculoBarato
from Vehiculo_grande import VehiculoGrande
from Base_de_datos import BaseDeDatos

def crear_vehiculo():
    """Implementa C (Create) del CRUD y pasos 1-4 para el objeto."""
    print("\n--- CREAR VEHÍCULO ---")
    tipo = input("Tipo (caro/barato/grande): ").lower()
    
    modelo = input("Modelo: ")
    color = input("Color: ")
    motor = input("Motor: ")
    num_puertas = int(input("Número de Puertas: "))
    capacidad_pasajeros = int(input("Capacidad de Pasajeros: "))
    tipo_combustible = input("Tipo de Combustible: ")
    
    nuevo_vehiculo = None
    
    if tipo == 'caro':
        descapotable = input("¿Es descapotable? (s/n): ").lower() == 's'
        nuevo_vehiculo = VehiculoCaro(modelo, color, motor, num_puertas, capacidad_pasajeros, tipo_combustible, descapotable)
    elif tipo == 'barato':
        capacidad_carga_kg = int(input("Capacidad de Carga (kg): "))
        nuevo_vehiculo = VehiculoBarato(modelo, color, motor, num_puertas, capacidad_pasajeros, tipo_combustible, capacidad_carga_kg)
    elif tipo == 'grande':
        peso_maximo_toneladas = float(input("Peso Máximo (toneladas): "))
        nuevo_vehiculo = VehiculoGrande(modelo, color, motor, num_puertas, capacidad_pasajeros, tipo_combustible, peso_maximo_toneladas)
    else:
        print("Tipo de vehículo no reconocido.")
        return

    exito, mensaje = BaseDeDatos.agregar_vehiculo(nuevo_vehiculo)
    print(mensaje)
    
    if exito:
        print("--- Prueba de Métodos (Arrancar) ---")
        print(nuevo_vehiculo.arrancar())
        print(nuevo_vehiculo.aceleracion_y_frenado(10))
        print("Vehículo creado y estado actual:\n", nuevo_vehiculo)
        
def leer_vehiculos():
    """Implementa R (Read) del CRUD."""
    print("\n--- LEER TODOS LOS VEHÍCULOS ---")
    vehiculos = BaseDeDatos.obtener_todos()
    if not vehiculos:
        print("No hay vehículos registrados.")
        return
        
    for i, vehiculo in enumerate(vehiculos):
        print(f"[{i+1}] {vehiculo}")

def actualizar_vehiculo():
    """Implementa U (Update) del CRUD."""
    print("\n--- ACTUALIZAR VEHÍCULO ---")
    leer_vehiculos()
    key = input("Ingrese la clave (Modelo-Color) del vehículo a actualizar (ej: Z4-Negro): ")
    vehiculo = BaseDeDatos.obtener_vehiculo(key)
    
    if vehiculo:
        print(f"Vehículo actual: {vehiculo}")
        
        nuevo_color = input("Nuevo color (dejar vacío para no cambiar): ")
        
        datos_actualizados = {}
        if nuevo_color:
            datos_actualizados['color'] = nuevo_color
            
        exito, mensaje = BaseDeDatos.actualizar_vehiculo(key, datos_actualizados)
        print(mensaje)
        
        if exito:
            print("--- Prueba de Métodos (Climatización) ---")
            print(vehiculo.climatizacion(22)) 
            print("Vehículo actualizado:\n", vehiculo)

    else:
        print(f"Vehículo con clave {key} no encontrado.")

def eliminar_vehiculo():
    """Implementa D (Delete) del CRUD."""
    print("\n--- ELIMINAR VEHÍCULO ---")
    leer_vehiculos() 
    key = input("Ingrese la clave (Modelo-Color) del vehículo a eliminar: ")
    vehiculo = BaseDeDatos.obtener_vehiculo(key)
    
    if vehiculo:
        print("--- Prueba de Métodos (Apagado) ---")
        print(vehiculo.apagado()) 
        exito, mensaje = BaseDeDatos.eliminar_vehiculo(key)
        print(mensaje)
    else:
        print(f"Vehículo con clave {key} no encontrado.")


def menu_principal():
    """Función principal que ejecuta el menú."""
    while True:
        print("\n==============================")
        print("  MENÚ PRINCIPAL - CRUD VEHÍCULOS")
        print("==============================")
        
    
        print("1. Crear Vehículo (Create / Pasos 1-7)")
        print("2. Ver Vehículos (Read / Paso 7)")
        print("3. Actualizar Vehículo (Update / Pasos 6-7)")
        print("4. Eliminar Vehículo (Delete / Pasos 6-7)")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            crear_vehiculo()
        elif opcion == '2':
            leer_vehiculos()
        elif opcion == '3':
            actualizar_vehiculo()
        elif opcion == '4':
            eliminar_vehiculo()
        elif opcion == '5':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    BaseDeDatos.agregar_vehiculo(VehiculoCaro("Z4", "Negro", "V6 Turbo", 2, 2, "Gasolina", True))
    BaseDeDatos.agregar_vehiculo(VehiculoBarato("Van", "Blanco", "4 Cilindros", 5, 2, "Diesel", 800))
    BaseDeDatos.agregar_vehiculo(VehiculoGrande("Camion", "Rojo", "V8 Diesel", 2, 3, "Diesel", 10.5))

    menu_principal()