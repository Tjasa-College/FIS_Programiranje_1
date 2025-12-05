# Mečemo 2 kocki dokler ne padeta 2 šestici.
# Program izpiše število metov, ko je bilo skupno število sodo.

import random

kocka1: int
kocka2: int
st_metov: int = 0

# Nastavimo izstopni pogoj in ga zanikamo
# Izstopimo, ko sta obe šestici.
while True:
    kocka1 = random.randint(1, 6)
    kocka2 = random.randint(1, 6)
    print(kocka1, kocka2, 'met', st_metov)

    # Če je liho število, preskočim nadaljnje izvajanje zanke
    if (kocka1 + kocka2) % 2 != 0:
        continue

    st_metov += 1
    if kocka1 == 6 and kocka2 == 6:
        break

print('Dve šestici sta padli v', st_metov, 'metu.')