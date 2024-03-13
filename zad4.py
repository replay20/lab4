from decimal import *

# jakim typem jest range ?
liczby = range(5)
print(type(liczby)) # range jest obiektem typu range (w Python 2.x była to lista)

# range może przyjmować 1 parametr, wtedy jest to parametr stop
for i in range(10):
    print(i)

# range może też przyjmować 2 parametry (start, stop)
for i in range(4, 10):
    print(i)

# lub 3 parametry (start, stop, step)
for i in range(4, 10, 2):
    print(i)

# możemy również generować wartości ujemne
for i in range(-5, -1):
    print(i)

for i in range(-5, -10, -2):
    print(i)

# lista z elementów funkcji range
lista = list(range(10))
print(lista)

# funkcja range nie generuje wartości zmiennoprzecinkowych, ale można
# dość łatwo taką funkcję stworzyć - poniżej funkcja generująca (yield)
def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step

for i in frange(0.1, 0.5, 0.1):
    print(i)

# po wyświetleniu wyniku można się zdziwić bo 0.3 to właściwie nie 0.3...
# to może jeszcze raz, ale tak
for i in frange(0.1, 0.5, 0.1):
    print(Decimal(i))

print((0.1 + 0.2) == 0.3)  # kto by się spodziewał ?
print(round((0.1 + 0.2), 2) == round(0.3, 2))  # teraz lepiej
print((Decimal(0.1) + Decimal(0.2)) == Decimal(0.3))
print((Decimal('0.1') + Decimal('0.2')) == Decimal('0.3'))