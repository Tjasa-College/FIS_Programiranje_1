def zadnji_znak(niz: str) -> str:
    return niz[-1]

last_char = lambda niz: niz[-1]

imena = ['Marko', 'Ajda', 'Katarina', 'Ivo', 'Petra', 'Aco', 'Zdenka', 'Lojze']

# Po abecedi
print(sorted(imena))

# Padajoče po abecedi
print(sorted(imena, reverse=True))

# Urejanje po dolžini imena tj. po dolžini niza.
print(sorted(imena, key=len))
# Padajoče
print(sorted(imena, key=len, reverse=True))

# Urejanje po zadnjem znaku.
print(sorted(imena, key=zadnji_znak))
print(sorted(imena, key=last_char))
print(sorted(imena, key=lambda niz: niz[-1]))
print(sorted(imena, key=lambda s: s[-1]))

# ------------------------------------------------------------
import math
nums = list(range(1,11))

# Klici funkcije map. Prvi parameter je funkcija.
print(list(map(math.sqrt, nums)))
print(list(map(abs, range(-5, 6))))

# Uporaba lambda funkcije
# Kvadrati števil od 1 do 10.
print(list(map(lambda x: pow(x, 2), range(1,11))))

# Potence števila 2 od 0 do 10
print(list(map(lambda x: pow(2, x), range(0,11))))

# Izpišimo imena, ki so daljša od 3 znakov.
print(list(filter(lambda s: len(s)>3, imena)))

# Izpišimo imena, i so krajša od 4 in daljša od 6 znakov..
print(list(filter(lambda s: len(s)<4 or len(s)>6, imena)))
