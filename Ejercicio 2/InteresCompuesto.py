class InteresCompuesto:
    def __init__(self, capital_inicial, tasa_interes, anios):
        self.capital_inicial = capital_inicial
        self.tasa_interes = tasa_interes / 100  # Convert percentage to decimal
        self.anios = anios

    def calcular_capital_final(self):
        return self.capital_inicial * (1 + self.tasa_interes) ** self.anios

