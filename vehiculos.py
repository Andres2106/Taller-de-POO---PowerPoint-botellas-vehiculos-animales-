#*********** ZONA DE FUNCIONES ************#
class Vehiculo:
    def __init__(self, modelo, color, motor, num_puertas, capacidad_pasajeros, tipo_combustible):
        self.modelo = modelo
        self.color = color
        self.motor = motor
        self.numero_puertas = num_puertas
        self.capacidad_pasajeros = capacidad_pasajeros
        self.tipo_combustible = tipo_combustible
        self.encendido = False
        self.velocidad = 0     

    def arrancar(self):
        """Método: Arrancar"""
        if not self.encendido:
            self.encendido = True
            return f"{self.modelo}: **Arrancado**. El motor está en marcha."
        else:
            return f"{self.modelo}: Ya está encendido."

    def apagado(self):
        """Método: Apagado"""
        if self.encendido and self.velocidad == 0:
            self.encendido = False
            return f"{self.modelo}: **Apagado**."
        elif self.velocidad > 0:
            return f"{self.modelo}: No se puede apagar, el vehículo está en movimiento."
        else:
            return f"{self.modelo}: Ya está apagado."
            
    def aceleracion_y_frenado(self, cambio_velocidad):
        """Método: Aceleración y Frenado (Ajusta la velocidad)"""
        if self.encendido:
            self.velocidad += cambio_velocidad
            if self.velocidad < 0:
                self.velocidad = 0
            return f"{self.modelo}: Velocidad actual: {self.velocidad} km/h."
        else:
            return f"{self.modelo}: No se puede acelerar ni frenar, el vehículo está apagado."

    def sistema_direccion(self, direccion):
        """Método: Sistema de Dirección"""
        return f"{self.modelo}: Girando la dirección hacia **{direccion}**."

    def climatizacion(self, temperatura):
        """Método: Climatización"""
        return f"{self.modelo}: Ajustando la climatización a {temperatura}°C."
    
    def luces(self, estado):
        """Método: Luces"""
        return f"{self.modelo}: Las luces están **{estado}**."

    def __str__(self):
        """Representación en string del objeto."""
        return (f"Modelo: {self.modelo} | Color: {self.color} | Motor: {self.motor} | "
                f"Puertas: {self.numero_puertas} | Pasajeros: {self.capacidad_pasajeros} | "
                f"Combustible: {self.tipo_combustible} | Estado: {'ENCENDIDO' if self.encendido else 'APAGADO'}")