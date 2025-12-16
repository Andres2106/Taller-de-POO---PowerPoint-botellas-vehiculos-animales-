#*************** ZONA DE FUNCIONES ***************#
class Botella: # 1. Crear clase
    _conteo_botellas = 0 # Atributo de clase para contar objetos

    def __init__(self, material, capacidad, forma, diseno, tapa, grabados): # 2. Hacer el constructor
        self._id = Botella._conteo_botellas # Asignar un ID único
        Botella._conteo_botellas += 1 # Incrementar el contador
        self._material = material # str: "Vidrio" o "Plástico"
        self._capacidad = capacidad # float o int: Capacidad en ml o L
        self._forma = forma # str
        self._diseno = diseno # str
        self._tapa = tapa # str
        self._grabados = grabados # bool

        # Atributos de estado para métodos
        self._esta_llena = False
        self._contenido_actual = 0 # Inicialmente vacía

    # Métodos (Implementando el punto 4. Crear métodos)
    # ----------------------------------------------------

    def contener_liquidos(self, cantidad):
        """Método para llenar la botella."""
        if self._contenido_actual + cantidad <= self._capacidad:
            self._contenido_actual += cantidad
            self._esta_llena = (self._contenido_actual == self._capacidad)
            return f"Botella {self._id} llena con {cantidad} unidades. Contenido total: {self._contenido_actual}"
        else:
            exceso = (self._contenido_actual + cantidad) - self._capacidad
            self._contenido_actual = self._capacidad
            self._esta_llena = True
            return f"¡ADVERTENCIA! Capacidad máxima alcanzada ({self._capacidad}). Se desbordaron {exceso} unidades."

    def facilitar_el_vertido(self, cantidad_a_verter):
        """Método para vaciar una parte de la botella (vertido)."""
        if self._contenido_actual >= cantidad_a_verter:
            self._contenido_actual -= cantidad_a_verter
            self._esta_llena = False
            return f"Se virtieron {cantidad_a_verter} unidades. Contenido restante: {self._contenido_actual}"
        else:
            verter = self._contenido_actual
            self._contenido_actual = 0
            self._esta_llena = False
            return f"Solo se pudo verter {verter} unidades (la botella estaba casi vacía). Contenido restante: 0"
    
    def cerrar_hermetico(self):
        """Simula el uso de la tapa."""
        return f"La botella {self._id} está ahora sellada herméticamente con una tapa de {self._tapa}."

    def reutlizacion(self):
        """Método que indica si la botella es reutilizable. Depende de si es Vidrio o Plástico."""
        # Se sobreescribirá en las subclases
        return f"La botella de {self._material} es reutilizable: NO ESPECIFICADO EN CLASE BASE."

    def transporte(self):
        """Método de estado de transporte."""
        return f"Botella {self._id} lista para el transporte."

    # Método de información general (para el punto 7: Retorno)
    def __str__(self):
        """Representación de string para imprimir la información del objeto."""
        estado = "llena" if self._esta_llena else "vacía/parcial"
        return (f"--- Botella ID: {self._id} ---\n"
                f"  Material: {self._material}\n"
                f"  Capacidad: {self._capacidad}u (Actual: {self._contenido_actual}u) -> Estado: {estado}\n"
                f"  Forma/Diseño: {self._forma} / {self._diseno}\n"
                f"  Tapa: {self._tapa} | Grabados: {'Sí' if self._grabados else 'No'}")