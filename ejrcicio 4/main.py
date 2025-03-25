
from mision import Mision
from colademisiones import ColaDeMisiones


def main():
    # Crear la cola de misiones
    cola = ColaDeMisiones()

    # Agregar misiones con diferentes niveles de dificultad
    cola.agregar_mision(Mision("Rescatar al aldeano", 3))
    cola.agregar_mision(Mision("Derrotar al dragón", 5))
    cola.agregar_mision(Mision("Explorar la cueva", 4))
    cola.agregar_mision(Mision("Explorar la cueva", 4))

    print("Misiones ordenadas por dificultad:")
    cola.mostrar_misiones()

    print("\nObteniendo misiones en orden de prioridad:")
    while True:
        mision = cola.obtener_siguiente_mision()
        if mision is None:
            break
        print(mision)


if __name__ == "__main__":
    main()