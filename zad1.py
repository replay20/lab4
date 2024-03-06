zdanie = input("Napisz dowolne zdanie: ")
print(zdanie)
print(type(zdanie))
licznik = 0

def Convert(string):
    lista = list (zdanie.split(" "))
    return lista

licz = Convert(zdanie)
for x in licz:
    licznik=licznik+1

print(licznik)