# Uporabnik vnese vhodne podatke: višino in radij stožca.
# Program izpiše volumen in površino stožca.
from math import *

r = int(input('Vpiši radij stožca:'))
v = int(input('Vpiši višino stožca:'))

s = sqrt(r ** 2 + v ** 2)

pov = pi * r ** 2 * pi * r * s
vol = pi * r ** 2 * v / 3

print('Volumen stožca je', pov)
print('Površina stožca je', vol)