import sys
sys.path.append('/C:/programacion/ej-Tema-1/Ejercicio 2')
from InteresCompuesto import InteresCompuesto

def main():
    capital_inicial = 1000
    while True:
        try:
            tasa_interes = float(input("Introduce la tasa de interés anual (entre 1% y 10%): "))
            if 1 <= tasa_interes <= 10:
                break
            else:
                print("La tasa de interés debe estar entre 1% y 10%.")
        except ValueError:
            print("Por favor, introduce un número válido.")

    while True:
        try:
            anios = int(input("Introduce el número de años: "))
            if anios > 0:
                break
            else:
                print("El número de años debe ser mayor a 0.")
        except ValueError:
            print("Por favor, introduce un número válido.")

    calculadora = InteresCompuesto(capital_inicial, tasa_interes, anios)
    capital_final = calculadora.calcular_capital_final()
    print(f"El capital final después de {anios} años será: {capital_final:.2f}")


if __name__ == "__main__":
    main()