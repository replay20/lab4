import sys as system

system.stdout.write("Podaj liczbe a: ")
a = system.stdin.readline()
a = int(a)
system.stdout.write("Podaj liczbe b: ")
b = system.stdin.readline()
b = int(b)
system.stdout.write("Podaj liczbe c: ")
c = system.stdin.readline()
c = int(c)

dzialanie = a ** b + c

system.stdout.write("Wynik dzialania: " + str(dzialanie))