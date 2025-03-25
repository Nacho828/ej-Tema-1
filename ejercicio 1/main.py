

def procesar_texto(texto):
    # Procesa el texto invirtiéndolo y eliminando números
    return ''.join(filter(lambda c: c.isalpha() or c.isspace(), texto[::-1]))


if __name__ == "__main__":
    # Ejemplo de uso
    texto_corrupto = "052 anozilaP"  # Ejemplo de texto corrupto
    texto_procesado = procesar_texto(texto_corrupto)
    print(texto_procesado)


