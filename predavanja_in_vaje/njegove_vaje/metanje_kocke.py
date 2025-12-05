# Fukcija enumerate za oštevilčenje.
# 1.000 krat vržem kocko.
# Program izpiše, kolikokrat je padla posamezna vrednost.
import random

števec = [0, 0, 0, 0, 0, 0]
# števec = [0] * 6

for i in range(1000):
    met = random.randint(1,6)
    števec[met-1] += 1

# Funkcija enumerate za oštevilčenje večelementne strukture.
print(list(enumerate(števec,1)))
rezultat = list(enumerate(števec,1))   # Seznam terk

# Izpisi
for pari in rezultat:  # (1, 135) ...
    print(pari)

for pik, metov in list(enumerate(števec,1)):
    print(f'Ševilo pik={pik}, je padlo {metov} krat.')