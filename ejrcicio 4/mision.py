class Mision:
    def __init__(self, nombre, dificultad):
        self.nombre = nombre
        self.dificultad = dificultad

    def __str__(self):
        return f"{self.nombre} (Dificultad: {self.dificultad})"
