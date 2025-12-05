# Štejemo koliko metov je bilo, da je prvič padla 6.

import random

# Inicializacija
stevec = 0

# Ponavljanje / izvajanje postopka
while True:
    kocka = random.randint(1, 6)
    stevec += 1
    print(kocka)
    if kocka == 6:
        break

# Izpis rezultatov
print('Kocko smo vrgli', stevec, 'krat.')