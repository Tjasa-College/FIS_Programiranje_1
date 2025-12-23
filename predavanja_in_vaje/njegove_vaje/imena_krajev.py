# Izpiše imena vseh krajev, iz katerih so zaposleni.
# ID;Priimek;Ime;Naslov;Pošta;Kraj;Datum rojstva;Spol;Izobrazba;Oddelek;Delovno mesto;Datum zaposlitve;Plača
# 1;Oblak;Miha;Glavni trg 12;3000;Celje;22.10.1953;m;VIII;Vodstvo;Direktor;1.01.2002;2.352,52 €

with open('Zaposleni.csv', encoding='utf-8-sig') as datoteka:
    next(datoteka)

    seznam_krajev = []
    for zaposleni in datoteka:
        oseba = zaposleni.split(';')
        kraj = oseba[5]
        if kraj not in seznam_krajev:
            seznam_krajev.append(kraj)

    print(seznam_krajev)
    print(len(seznam_krajev))