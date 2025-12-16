class Animal:
    def __init__(self, nombre, edad, habitat, dieta, tamano, color):
        self.__nombre = nombre
        self.__edad = edad
        self.__habitat = habitat
        self.__dieta = dieta
        self.__tamano = tamano
        self.__color = color

    def moverse(self):
        """Método abstracto: cada animal se mueve diferente."""
        return f"El animal {self.__nombre} se está moviendo."

    def comunicarse(self):
        """Método genérico para la comunicación."""
        return f"{self.__nombre} está haciendo un sonido."

    def alimentarse(self):
        return f"{self.__nombre} está comiendo su dieta de {self.__dieta}."

    def dormir(self):
        return f"{self.__nombre} está durmiendo (Descanso/Sueño)."

    def get_info(self):
        """Retorna todos los atributos del animal."""
        return {
            "Nombre": self.__nombre,
            "Edad": self.__edad,
            "Hábitat": self.__habitat,
            "Dieta": self.__dieta,
            "Tamaño": self.__tamano,
            "Color": self.__color
        }
        
    def actualizar_edad(self, nueva_edad):
        """Permite actualizar la edad del animal."""
        self.__edad = nueva_edad
        return f"¡Edad de {self.__nombre} actualizada a {nueva_edad} años!"

    def get_nombre(self):
        return self.__nombre  