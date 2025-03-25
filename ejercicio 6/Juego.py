class Juego:
    def __init__(self):
        self.personajes = []

    def agregar_personaje(self, personaje):
        self.personajes.append(personaje)

    def separar_personajes(self):
        humanos = [personaje.nombre for personaje in self.personajes if personaje.es_humano]
        no_humanos = [personaje.nombre for personaje in self.personajes if not personaje.es_humano]
        return sorted(humanos), sorted(no_humanos)
