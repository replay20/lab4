def wiezaA(a):
    for i in range(a + 1):
        print("A" * i)


a = input("Podaj wysokosc wiezy (nie wiecej niz 10): ")
a = int(a)


if (a<=10) & (a>0):
    wiezaA(a)
else:
    print("Podano zla wartosc")