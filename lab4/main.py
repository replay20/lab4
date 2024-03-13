import random
import sys as system

def utworzWektor(n):
    suma = 0
    zwrotSuma = suma
    for i in range(n):
        for j in range(n):
            liczbaLosowa = random.randint(1, 100)
            suma += liczbaLosowa
            system.stdout.write(str(liczbaLosowa) + " ")
        print("Suma wiersza nr " + str(i + 1) + " " + str(suma))
        zwrotSuma += suma
        suma = 0
    return zwrotSuma


print(utworzWektor(6))