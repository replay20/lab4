liczba = input("Podaj liczbe: ")
liczba = int(liczba)

czyPierwsza = True

if liczba <= 1 :
    czyPierwsza = False
elif liczba > 1 :
    for i in range(2,liczba):
        if (liczba % i) == 0:
            czyPierwsza = False
            break

if czyPierwsza == True:
    print(liczba, "jest liczba pierwsza")
else:
    print(liczba, "nie jest liczba pierwsza")