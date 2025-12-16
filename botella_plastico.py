class Botella_plastico: # Hereda de Botella
    
    def __init__(self, capacidad, forma, diseno, tapa="rosca", grabados=False):
        # Llama al constructor de la clase padre (Botella)
        super().__init__("Plástico", capacidad, forma, diseno, tapa, grabados)
        self._es_ligero = True # Atributo específico de plástico

    # Sobreescritura del método para compatibilidad
    def compatibilidad_bebidas_calientes_frias(self, temperatura):
        if 5 <= temperatura <= 60:
            return f"El plástico es compatible con bebidas a {temperatura}°C."
        return "ADVERTENCIA: Temperatura fuera del rango seguro, posible liberación de químicos o deformación."

    # Sobreescritura del método para reutilización (limitada)
    def reutlizacion(self):
        return f"La botella de {self._material} es **REUTILIZABLE LIMITADAMENTE** (Menor vida útil)."