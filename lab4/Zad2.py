def wiezaA(a):
    for i in range(a + 1):
        print("A" * i)


a = input("Podaj wysokosc wiezy (nie wiecej niz 10): ")

if(a<=10 & a>0):
    wiezaA(int(a))
else:
    print("Podano zla wartosc")