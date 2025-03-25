class PalabrasComunes:
    def __init__(self, lista1, lista2):
        self.lista1 = lista1
        self.lista2 = lista2

    def encontrarcomunes(self):
        return list(set(self.lista1) & set(self.lista2))