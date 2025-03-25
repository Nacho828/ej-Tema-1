class Personaje:
    def __init__(self, nombre, es_humano):
        self.nombre = nombre
        self.es_humano = es_humano

def separar_personajes(personajes):
    humanos = []
    no_humanos = []
    for personaje in personajes:
        if personaje.es_humano:
            humanos.append(personaje.nombre)
        else:
            no_humanos.append(personaje.nombre)
    return sorted(humanos), sorted(no_humanos)