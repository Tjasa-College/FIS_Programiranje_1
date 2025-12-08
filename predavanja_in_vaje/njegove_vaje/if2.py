# Uporabnik vnese starost.
# Mi izpišemo ali je polnoleten.
# Izpišimo še, koliko let je od tega.

starost = int(input('Vnesi starost v letih:'))

if starost < 18:
    print('Si mladoleten.')
    print('Manjka ti še', 18 - starost, 'let.')
else:
    print('Polnoleten si.')
    print('Že', starost - 18, 'let.')

print('Konec programa.')