# Loto je 7 naključnih različnih števil med 1 in 39.
# Izpišimo urejeno.

import random

loto = []   # Nimamo še nobenega števila.

while len(loto) < 7:
    število = random.randint(1,39)
    if število not in loto:
        loto.append(število) # Dodam na seznam

loto.sort()    # Tukaj samo uredimo
print(loto)