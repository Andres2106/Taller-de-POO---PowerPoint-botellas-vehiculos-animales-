class Botella_vidrio: # Hereda de Botella

    def __init__(self, capacidad, forma, diseno, tapa="corcho", grabados=True):
        # Llama al constructor de la clase padre (Botella)
        super().__init__("Vidrio", capacidad, forma, diseno, tapa, grabados)
        self._transparencia = True # Atributo específico de vidrio

    # Sobreescritura del método para compatibilidad
    def compatibilidad_bebidas_calientes_frias(self, temperatura):
        if -20 <= temperatura <= 100:
            return f"El vidrio es compatible con bebidas a {temperatura}°C."
        return "ADVERTENCIA: Temperatura extrema, riesgo de fractura del vidrio."

    # Sobreescritura del método para reutilización (más duradero)
    def reutlizacion(self):
        return f"La botella de {self._material} es **ALTAMENTE REUTILIZABLE** (Larga vida útil)."