import sys as system

def wiezaA(a):
    iloscSpacji = a
    iloscA = 1

    for i in range(a):
        for j in range(iloscSpacji):
            system.stdout.write(" ")
        system.stdout.write("A" * iloscA)
        system.stdout.write("\n")
        iloscA+=2
        iloscSpacji-=1


a = input("Podaj wysokosc wiezy (nie wiecej niz 10): ")
a = int(a)


if (a<=10) & (a>0):
    wiezaA(a)
else:
    print("Podano zla wartosc")