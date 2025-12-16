class Caballo(Animal):
    def moverse(self):
        return f"{self.get_nombre()} galopa con fuerza por la pradera."
    
class Cocodrilo(Animal):
    def moverse(self):
        return f"{self.get_nombre()} se arrastra lentamente o nada en el agua."

class Pez(Animal):
    def moverse(self):
        return f"{self.get_nombre()} nada rápidamente en el acuario."

class Escarabajo(Animal):
    def moverse(self):
        return f"{self.get_nombre()} vuela torpemente y camina sobre la hoja."

class Pato(Animal):
    def moverse(self):
        return f"{self.get_nombre()} camina en tierra y nada tranquilamente."