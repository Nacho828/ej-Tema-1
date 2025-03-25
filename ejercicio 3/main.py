from Palabras import PalabrasComunes

def main():
    lista1 = ["manzana", "pera", "uva", "manzana", "naranja"]
    lista2 = ["pera", "kiwi", "uva", "naranja", "naranja"]

    palabras = PalabrasComunes(lista1, lista2)
    resultado = palabras.encontrarcomunes()
    print("Palabras comunes:", resultado)

if __name__ == "__main__":
    try:
        main()
    except ImportError as e:
        print(f"Error al importar: {e}")
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")