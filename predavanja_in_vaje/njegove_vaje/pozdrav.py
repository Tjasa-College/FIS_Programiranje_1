# Program, ki upranika povpraša po imenu in starosti.
# Uporabnika pozdravi in izpiše, koliko časa je že polnoleten.

'Tudi tole je lahko komentar.'

besedilo = ''' Tole je 
   večvrstični
    komentar.
'''

ime = input('Vpiši svoje ime:')
starost = int(input('Koliko si star:'))  # Takoj pretvorim v celo število.

print('Pozdravljen',ime, 'Kako si?')
print('Polnoleten si že', starost - 18, 'let')

print(besedilo)