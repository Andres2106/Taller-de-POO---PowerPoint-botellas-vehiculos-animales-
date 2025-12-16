# BASE DE DATOS EN MEMORIA
registro_animales = {} 

# C: Crear 
def crear_animal(clase_animal, nombre, edad, habitat, dieta, tamano, color):
    if nombre in registro_animales:
        return f"Error: Ya existe un animal llamado {nombre}."
    
    nuevo_animal = clase_animal(nombre, edad, habitat, dieta, tamano, color)
    # >>> INSERCIÓN EN LA BASE DE DATOS <<<
    registro_animales[nombre] = nuevo_animal 
    return f"Animal **{nombre}** creado y registrado con éxito. (Tipo: {clase_animal.__name__})"

# R: Leer
def leer_animal(nombre):
    # >>> BÚSQUEDA POR CLAVE <<<
    animal = registro_animales.get(nombre) 
    # ... resto de la lógica ...

def listar_animales():
    # >>> ITERACIÓN SOBRE LAS CLAVES <<<
    for nombre, animal_obj in registro_animales.items():
        # ... resto de la lógica ...

# U: Actualizar 
def actualizar_animal(nombre, nueva_edad):
    # >>> BÚSQUEDA POR CLAVE <<<
    animal = registro_animales.get(nombre)
    # ... resto de la lógica ...

# D: Eliminar
def eliminar_animal(nombre):
    if nombre in registro_animales:
        # >>> ELIMINACIÓN DE CLAVE-VALOR <<<
        del registro_animales[nombre]
        print(f"Animal {nombre} eliminado del registro.")
    # ... resto de la lógica ...