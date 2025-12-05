# Vprašaj uporabnika po imenu in starosti.
# Izpiši koliko časa je že polnoleten.

ime = input('Vpiši svoje ime:')
starost = input('Vpiši starost v letih:')
starost = int(starost)

print('Dober dan', ime, ', kako si kaj?')

st_let = starost - 18
print('Polnoleten si že', st_let,'let.')