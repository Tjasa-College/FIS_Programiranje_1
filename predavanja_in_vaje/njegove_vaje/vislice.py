# En uporabnik vnese skriti stavek.
# Drugi uganjuje. Velikost znakov ni pomembna.
# Ločil ne uganjuje.
# Začetno stanje uganke izpiše v naslednji obliki:
# Živjo! Kako si kaj?
# _ _ _ _ _ !   _ _ _ _   _ _  _ _ _ ?
# Na koncu izpiše kolikokrat je ugibal in si sproti
# posodablja stanje.

stavek = input('Vnesi skriti stavek:').upper()

# 1. izpis stanja.
#   - znake izpisuje s črtico, ločila izpišem normalno
locila = ' ,.!?:;'
ugibani_znaki = ''

while True:
    # Izpis trenutnega stanja
    uganka = ''
    for char in stavek:
        if char in locila or char in ugibani_znaki:
            uganka += char + ' '
        else:
            uganka += '_ '
    print(uganka)

    # Če ni nobene črtice v uganki, je rešil in končamo.
    if uganka.count('_') == 0:
        break

    # Uganjevanje
    poizkus = input('Vnesi znak:').upper()
    ugibani_znaki += poizkus

print(f'Uganil si v {len(ugibani_znaki)} poizkusih.')