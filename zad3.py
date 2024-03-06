slowo = input("Podaj slowo: ")



def palin(slowo):

    dlug = len(slowo)

    for i in range(dlug):
        if slowo[i] != slowo[-i -1]:
            return False
        else:
            return True

print(palin(slowo))