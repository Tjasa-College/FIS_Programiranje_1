# Program izpiše število oseb po posameznih oddelikih.
'''
ID;Priimek;Ime;Naslov;Pošta;Kraj;Datum rojstva;Spol;Izobrazba;Oddelek;Delovno mesto;Datum zaposlitve;Plača
1;Oblak;Miha;Glavni trg 12;3000;Celje;22.10.1953;m;VIII;Vodstvo;Direktor;1.01.2002;2.352,52 €
'''

import matplotlib.pyplot as plt

# Uporaba slovarja kot števca.
oddelki = {}
with open('Zaposleni.csv', mode='r', encoding='utf-8-sig') as vhodna:
    vhodna.readline(    )  # Preskok glave
    for vrstica in vhodna:
        oseba = vrstica.split(';')
        oddelek = oseba[9]
        if oddelek in oddelki:
            oddelki[oddelek] += 1
        else:
            oddelki[oddelek] = 1

# Izpis slovarja kot strukture
print(oddelki)

# Izpis po tuple-ih
for oddelek in oddelki.items():
    print(oddelek)

# Izpis konkretnih podatkov
for ključ, vrednost in oddelki.items():
    print(ključ, vrednost)

plt.title('Kadrovska sestava oddelkov')
plt.bar(oddelki.keys(), oddelki.values())
plt.xlabel('Oddelki')
plt.xticks(rotation=90)
plt.ylabel('Število oseb')
plt.show()