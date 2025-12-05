# Mečemo 2 kocki dokler ne padeta 2 šestivi.
# Program izpiše število metov.

import random

kocka1: int = random.randint(1,6)
kocka2: int = random.randint(1,6)
st_metov: int = 1
print(kocka1, kocka2)

# Nastavimo izstopni pogoj in ga zanikamo
# Izstopimo, ko sta obe šestici.
while not (kocka1 == 6 and kocka2 == 6):
    kocka1 = random.randint(1, 6)
    kocka2 = random.randint(1, 6)
    print(kocka1, kocka2)
    st_metov += 1

print('Dve šestici sta padli v', st_metov, 'metu.')