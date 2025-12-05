# Seznam v vlogi števca.
# 1.000 krat vržemo kocko.
# Izpišemo, kolikokrat je padla posamezna vrednost
from random import *

vrednosti = [0] * 6

for met in range(1000):
    kocka = randint(1,6)
    vrednosti[kocka-1] += 1
    #print(kocka)

print(met, vrednosti)