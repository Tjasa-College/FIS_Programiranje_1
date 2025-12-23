# Izpiše imena vseh krajev, iz katerih so zaposleni.
# ID;Priimek;Ime;Naslov;Pošta;Kraj;Datum rojstva;Spol;Izobrazba;Oddelek;Delovno mesto;Datum zaposlitve;Plača
# 1;Oblak;Miha;Glavni trg 12;3000;Celje;22.10.1953;m;VIII;Vodstvo;Direktor;1.01.2002;2.352,52 €

with open('Zaposleni.csv', encoding='utf-8-sig') as datoteka:
    next(datoteka)

    # Rešitev z uporabo množice
    mn_krajev = set()
    for zaposleni in datoteka:
        oseba = zaposleni.split(';')
        kraj = oseba[5]
        mn_krajev.add(kraj)

    print(sorted(mn_krajev))
    print(len(mn_krajev))