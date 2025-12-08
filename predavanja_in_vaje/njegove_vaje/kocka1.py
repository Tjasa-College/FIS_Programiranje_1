# Štejemo koliko metov je bilo, da je prvič padla 6.

import random

# Inicializacija
stevec = 0
kocka = random.randint(1,6)
stevec += 1
print('Prvi met', kocka)

# Ponavljanje / izvajanje postopka
while kocka != 6:
    kocka = random.randint(1, 6)
    stevec += 1
    print(kocka)

# Izpis rezultatov
print('Kocko smo vrgli', stevec, 'krat.')