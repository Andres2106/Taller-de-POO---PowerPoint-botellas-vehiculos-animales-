class VehiculoBarato:
    """Representa un vehículo barato (utilitario/carga pequeña)."""
    
    def __init__(self, modelo, color, motor, num_puertas, capacidad_pasajeros, tipo_combustible, capacidad_carga_kg):
        super().__init__(modelo, color, motor, num_puertas, capacidad_pasajeros, tipo_combustible)
        self.capacidad_carga_kg = capacidad_carga_kg

    def sistema_de_seguridad(self):
        """Método: Sistema de Seguridad (Básico)"""
        return f"{self.modelo}: Sistema de seguridad: **Airbags y ABS operativos**."
        
    def sistema_de_espejo(self):
        """Método: Sistema de Espejo (Manual)"""
        return f"{self.modelo}: Espejos **manuales** revisados."

    def __str__(self):
        return super().__str__() + f" | Carga Máxima: {self.capacidad_carga_kg} kg"