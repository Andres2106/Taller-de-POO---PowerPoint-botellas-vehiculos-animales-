class VehiculoGrande:
    """Representa un vehículo grande (Camión/Bus)."""
    
    def __init__(self, modelo, color, motor, num_puertas, capacidad_pasajeros, tipo_combustible, peso_maximo_toneladas):
        super().__init__(modelo, color, motor, num_puertas, capacidad_pasajeros, tipo_combustible)
        self.peso_maximo_toneladas = peso_maximo_toneladas
    
    def sistema_de_seguridad(self):
        """Método: Sistema de Seguridad (Especial para vehículos pesados)"""
        return f"{self.modelo}: Sistema de seguridad con **freno de motor** operativo."
        
    def sistema_de_espejo(self):
        """Método: Sistema de Espejo (Panorámico)"""
        return f"{self.modelo}: Espejos **panorámicos** ajustados para visión amplia."

    def aceleracion_y_frenado(self, cambio_velocidad):
        """Método: Aceleración y Frenado (Más lento para vehículos grandes)"""
        if self.encendido:
            cambio_real = cambio_velocidad * 0.5 
            self.velocidad += cambio_real
            if self.velocidad < 0:
                self.velocidad = 0
            return f"{self.modelo}: Velocidad actual: {int(self.velocidad)} km/h (Vehículo pesado)."
        else:
            return f"{self.modelo}: No se puede acelerar ni frenar, el vehículo está apagado."
            
    
    def __str__(self):
        return super().__str__() + f" | Peso Máximo: {self.peso_maximo_toneladas} ton"