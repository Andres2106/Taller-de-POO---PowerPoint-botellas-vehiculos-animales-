class VehiculoCaro:
    """Representa un vehículo caro (Deportivo/Lujo)."""
    
    def __init__(self, modelo, color, motor, num_puertas, capacidad_pasajeros, tipo_combustible, descapotable=False):
        super().__init__(modelo, color, motor, num_puertas, capacidad_pasajeros, tipo_combustible)
        self.descapotable = descapotable

    def sistema_de_seguridad(self):
        """Método: Sistema de Seguridad (Añade una característica de seguridad avanzada)"""
        return f"{self.modelo}: Sistema de seguridad avanzado (Asistencia de carril) **ACTIVADO**."
        
    def sistema_de_espejo(self):
        """Método: Sistema de Espejo (Añade una característica de espejo avanzado)"""
        return f"{self.modelo}: Espejos **electrocromáticos** ajustados."

    def sistema_de_ventanas(self, estado):
        """Método: Sistema de Ventanas (Añade una característica de ventana avanzada)"""
        if self.descapotable:
            return f"{self.modelo}: Techo retráctil y ventanas **{estado}**."
        else:
            return super().sistema_de_ventanas(estado)
        
    def __str__(self):
        return super().__str__() + f" | Descapotable: {self.descapotable}"