import geografija

# Program naj izpiše imena kontinentov in njihovo skupno površino.

continents = geografija.kontinenti('Geografija.csv')
states = geografija.opisi_drzav('Geografija.csv')

for continent in continents:
    area = geografija.kont_povr(states, continent)
    print(f'{continent:15} {area:10,d}')