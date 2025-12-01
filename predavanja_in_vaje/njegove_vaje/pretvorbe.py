# Uporabnik vnese stopinje in enote.
# Enote vnese s črkami C, c, F, f, K, k
# Stopinje vnese s celo številko.
# Program izpiše v stopinjah celzija.

enote = input('Vnesi črko za enote:')
stop = int(input('Vnesi stopinje:'))

match enote:
    case 'C' | 'c':
        print(stop, '°C')
    case 'F' | 'f':
        fahr = (stop - 32) * (5/9)
        print(fahr, '°F')
    case 'K' | 'k':
        kelv = stop + 273.15
        print(kelv, '°K')
    case _ :
        print('Neznana enota.')
