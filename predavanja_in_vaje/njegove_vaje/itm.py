# Funkcija za izračun itm
def itm(masa: float, višina: int) -> float:
    return masa / (višina/100) ** 2

# Funkcija za izpis stanja glede na itm
def itm_stanje(indeks_itm: float) -> str:
    if indeks_itm < 18.5:
        return 'Suhost'
    elif indeks_itm < 25:
        return 'Normalna telesna masa'
    elif indeks_itm < 30:
        return 'Povečana telesna masa'
    else:
        return 'Debelost'

def itm_komplet(masa: float, višina: int):
    ix = itm(masa, višina)
    st = itm_stanje(ix)
    return ix, st

teža = float(input('Vnesi težo v kg:'))
višina = int(input('Vnesi višino v cm:'))

moj_itm = itm(teža, višina)
moje_stanje = itm_stanje(moj_itm)

print('Tvoj itm:', moj_itm)
print('Tvoje stanje:', moje_stanje)
print('Komplet:', itm_komplet(teža, višina))