# Program, ki predlaga loto kombinacijo
# Loto kombinacija je 7 različnih števil na intervalu od 1 do 39
# Izpišimo naraščajoče urejeno loto kombinacijo

from random import *

# Na začetku nimam še nobebe izžrebane številke
loto = []

while len(loto) < 7:
    kandidat = randint(1,39)  # Izžrebam
    if kandidat not in loto:
        loto.append(kandidat)
        # loto += [kandidat]

loto.sort()   # Metoda samo sortirna in nič ne vrača.
              # Zato tega stavka ne smemo uporabiti v print.
print(loto)