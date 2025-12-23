# Izpiše množice delovnih mest po posameznih oddelkih.
# ID;Priimek;Ime;Naslov;Pošta;Kraj;Datum rojstva;Spol;Izobrazba;Oddelek;Delovno mesto;Datum zaposlitve;Plača
# 1;Oblak;Miha;Glavni trg 12;3000;Celje;22.10.1953;m;VIII;Vodstvo;Direktor;1.01.2002;2.352,52 €

with open('Zaposleni.csv', encoding='utf-8-sig') as datoteka:
    next(datoteka)

    delovna_mesta = {}  # Slovar množic
    for zaposleni in datoteka:
        oseba = zaposleni.split(';')
        oddelek = oseba[9]
        dmesto = oseba[10]
        if oddelek not in delovna_mesta:
            delovna_mesta[oddelek] = set()
        delovna_mesta[oddelek].add(dmesto)

    print(delovna_mesta)