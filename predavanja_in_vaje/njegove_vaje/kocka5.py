# Štejemo koliko metov je bilo, da je prvič padla 6.

import random

# Inicializacija
stevec = 0


# Ponavljanje / izvajanje postopka
while (kocka := random.randint(1,6)) != 6:
    stevec += 1
    print(kocka)
else:
    print(kocka)

# Izpis rezultatov
print('Kocko smo vrgli', stevec + 1, 'krat.')