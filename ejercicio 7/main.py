from Inventario import Inventario

def main():
    inventario = Inventario()

    try:
        inventario.agregar_item("Espada")
        inventario.agregar_item("Escudo")
        inventario.agregar_item("Espada")  # Esto debería lanzar un ValueError
    except ValueError as e:
        print(e)

    print("Inventario actual:", inventario.mostrar_inventario())


if __name__ == "__main__":
    main()