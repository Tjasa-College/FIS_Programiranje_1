# Uporabnik vpiše svoj EMŠO
# Program izpiše njegov datum rojstva in spol
# 0123456789012
# DDMMLLLrrSccc
# S - 0-4 --> Moški, 5 - 9 --> Ženska
# datum izpišemo takole: 12.07.2001

emso = input('Vpiši svoj EMŠO:')

# Preverjamo veljavnost emso. Dolžina mora biti 13 in same cifre.
if len(emso) == 13 and emso.isnumeric():
    dan = emso[:2]
    mesec = emso[2:4]
    leto = emso[4:7]

    if leto[0] == '9':
        leto = '1' + leto
    else:
        leto = '2' + leto

    # Idntična koda
    #if int(leto[0]) == 9:
    #    leto = '1' + leto
    #else:
    #    leto = '2' + leto

    datum = dan + '.' + mesec + '.' + leto
    datum2 = f'{dan}.{mesec}.{leto}'

    print(datum)
    print(datum2)
    print(f'{dan}.{mesec}.{leto}')

    # Izpis spola
    if int(emso[-4]) < 5:
        print('Moški')
    else:
        print('Ženska')

    if emso[-4] in '01234':
        print('MOŠKI')
    else:
        print('ŽENSKA')
else:
    print('EMŠO ni veljaven.')
