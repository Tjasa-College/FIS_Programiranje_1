# Koliko metov je bilo potrebnih, da 100 krat pade 6?

import random

# Inicializacija
st_metov = 0
st_sestic = 0

# Ponavljanje / izvajanje postopka
while st_sestic < 100:
    kocka = random.randint(1, 6)
    st_metov += 1
    print(kocka)
    if kocka == 6:
        st_sestic += 1
        print('Šestice', st_sestic)

# Izpis rezultatov
print('Kocko smo vrgli', st_metov, 'krat, da je 100. padla šestica.')