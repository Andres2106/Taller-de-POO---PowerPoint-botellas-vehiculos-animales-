class BaseDeDatos:
    """Simula una base de datos para almacenar objetos Vehiculo."""
    _vehiculos = {}

    @classmethod
    def agregar_vehiculo(cls, vehiculo):
        """Método C (Create) para agregar un vehículo."""
        key = f"{vehiculo.modelo}-{vehiculo.color}"
        if key not in cls._vehiculos:
            cls._vehiculos[key] = vehiculo
            return True, f"Vehículo {vehiculo.modelo} agregado con éxito."
        else:
            return False, f"Error: Vehículo {vehiculo.modelo}-{vehiculo.color} ya existe."

    @classmethod
    def obtener_vehiculo(cls, key):
        """Método R (Read) para obtener un vehículo por su clave."""
        return cls._vehiculos.get(key)

    @classmethod
    def obtener_todos(cls):
        """Método R (Read) para obtener todos los vehículos."""
        return list(cls._vehiculos.values())

    @classmethod
    def actualizar_vehiculo(cls, key, nuevos_datos):
        """Método U (Update) para actualizar los datos de un vehículo."""
        if key in cls._vehiculos:
            vehiculo = cls._vehiculos[key]
            if 'color' in nuevos_datos:
                vehiculo.color = nuevos_datos['color']
            return True, f"Vehículo {key} actualizado con éxito."
        else:
            return False, f"Error: Vehículo con clave {key} no encontrado."

    @classmethod
    def eliminar_vehiculo(cls, key):
        """Método D (Delete) para eliminar un vehículo."""
        if key in cls._vehiculos:
            del cls._vehiculos[key]
            return True, f"Vehículo con clave {key} eliminado con éxito."
        else:
            return False, f"Error: Vehículo con clave {key} no encontrado."