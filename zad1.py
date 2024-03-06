zdanie = input("Napisz dowolne zdanie: ")
print(zdanie)
print(type(zdanie))

def Convert(string):
    lista = list (zdanie.split(" "))
    return lista

print (Convert(zdanie))