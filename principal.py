# Base_de_datos.py
class Base_de_datos:
    """Clase que simula una base de datos para almacenar objetos Botella."""
    
    def __init__(self):
        self._almacenamiento = [] # Lista para guardar los objetos Botella

    # Operaciones CRUD
    
    def crear_botella(self, botella):
        """CREATE: Agrega un nuevo objeto Botella."""
        self._almacenamiento.append(botella)
        return True

    def leer_todas_las_botellas(self):
        """READ: Devuelve la lista completa de botellas."""
        return self._almacenamiento

    def buscar_botella_por_id(self, id_botella):
        """READ: Busca una botella por su ID."""
        for botella in self._almacenamiento:
            if botella._id == id_botella:
                return botella
        return None

    def actualizar_botella(self, id_botella, nuevo_diseno):
        """UPDATE: Actualiza el atributo 'diseño' de una botella específica."""
        botella = self.buscar_botella_por_id(id_botella)
        if botella:
            botella._diseno = nuevo_diseno
            return True
        return False

    def eliminar_botella(self, id_botella):
        """DELETE: Elimina una botella por su ID."""
        botella = self.buscar_botella_por_id(id_botella)
        if botella:
            self._almacenamiento.remove(botella)
            return True
        return False