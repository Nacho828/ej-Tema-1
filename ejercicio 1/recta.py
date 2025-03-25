class Receta:
    def __init__(self, texto_corrupto):
        self.texto_corrupto = texto_corrupto

    def procesar_texto(self):
        # Voltear la cadena
        texto_volteado = self.texto_corrupto[::-1]
        # Dividir el texto en nombre y calorías
        partes = texto_volteado.split(" ", 1)
        self.nombre_receta = partes[1]
        self.calorias = partes[0]

    def mostrar_receta(self):
        return f"La receta de {self.nombre_receta} contiene {self.calorias} calorías."