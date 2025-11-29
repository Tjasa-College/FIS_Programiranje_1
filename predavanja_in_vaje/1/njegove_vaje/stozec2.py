# Uporabnik vnese vhodne podatke: višino in radij stožca.
# Program izpiše volumen in površino stožca.
import math

r = int(input('Vpiši radij stožca:'))
v = int(input('Vpiši višino stožca:'))

s = math.sqrt(r ** 2 + v ** 2)

pov = math.pi * r ** 2 * math.pi * r * s
vol = math.pi * r ** 2 * v / 3

print('Volumen stožca je', pov)
print('Površina stožca je', vol)