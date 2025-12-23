# CountryCode;Name;IndepYear;Region;Continent;SurfaceArea;HeadOfState;GovernmentForm;GNP;Population;LifeExpectancy
# ABW;Aruba;;Caribbean;North America; 193 ;Beatrix;Nonmetropolitan Territory of The Netherlands; $828 ; 103.000 ;78,4

'''
Funkcija z imenom opisi_drzav(ime_datoteke), ki vrne seznam držav. Vsaka država na seznamu je predstavljena s slovarjem. Za ključe slovarja uporabite imena stolpcev iz glave tabele. Numerične vrednosti pretvorite v ustrezno vrednost za nadaljnje računanje. Vhodni parameter je ime_datoteke, v kateri so podatki.
Funkcija z imenom kont_povr(drzave, kontinent), ki za podani kontinent izračuna skupno površino. Prvi parameter je seznam držav iz 2. naloge, drugi parameter pa ime celine. Vrne vrednost v celoštevilski obliki.
Funkcija z imenom kont_pop(drzave, kontinent), ki za podani kontinent izračuna skupno populacijo. Prvi parameter je seznam držav iz 2. naloge, drugi parameter pa ime celine.  Vrne vrednost v celoštevilski obliki.
'''

def opisi_drzav(ime_datoteke: str) -> list[dict]:
    with open(ime_datoteke, encoding='utf-8-sig') as datoteka:
        glava = datoteka.readline().strip().split(';')
        states = []
        for vrstica in datoteka:
            podatki = vrstica.strip().split(';')
            # Ustavim slovar, kjer je prvi element ime stolpca, drugi pa konkretni podatek države.
            država = dict(zip(glava, podatki))
            states.append(država)
    return states

def kont_povr(drzave: list[dict], kontinent: str) -> int:
    skupna_povr = 0
    for state in drzave:
        if state['Continent'] == kontinent:
            skupna_povr += int(state['SurfaceArea'].replace('.',''))
    return skupna_povr

def kont_pop(drzave, kontinent):
    ...

def kontinenti(ime_datoteke: str) -> set:
    continents = set()
    with open(ime_datoteke, encoding='utf-8-sig') as datoteka:
        datoteka.readline()
        for vrstica in datoteka:
            continents.add(vrstica.split(';')[4])
    return continents

if __name__ == '__main__':
    print('Vrednost spremenljivke __name__:', __name__)
    print('+++', kontinenti('Geografija.csv'))
    cont = kontinenti('Geografija.csv')

    print(opisi_drzav('Geografija.csv'))
    države = opisi_drzav('Geografija.csv')

    print(kont_povr(države, 'Europe'))

