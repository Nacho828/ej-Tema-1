from Personaje import Personaje
from Juego import Juego


def main():
    juego = Juego()
    juego.agregar_personaje(Personaje("Mario", True))
    juego.agregar_personaje(Personaje("Link", True))
    juego.agregar_personaje(Personaje("Pikachu", False))
    juego.agregar_personaje(Personaje("Kirby", False))
    juego.agregar_personaje(Personaje("Samus", True))

    humanos, no_humanos = juego.separar_personajes()
    print("Humanos:", humanos)
    print("No Humanos:", no_humanos)

if __name__ == "__main__":
    main()
