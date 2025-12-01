# Program vpraša po temperaturi vode in po enotah.
# Enote uporabnik vnese z znaki C, F ali K.
# Izpisati želimo agregatno stanje vode:
#     led, tekočina, para

stopinje = int(input('Vnesi temperaturo vode:'))
enote = input('Vnesi enote [C,F,K]:')

match enote:
    case 'C':
        print('Celzij')
        celzij = stopinje
    case 'K':
        print('Kelvini')
        celzij = stopinje - 273.15
    case 'F':
        print('Fahrenheiti')
        celzij = (stopinje - 32) * 5 / 9

if celzij < 0:
    print('Led')
elif celzij > 100:
    print('Para')
else:
    print('Tekočina')

print(f'Voda ima teperaturo {celzij:0.2f}°C.')