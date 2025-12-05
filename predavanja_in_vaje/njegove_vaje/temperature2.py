# Uporabnik vpiše temperaturo vode v °F.
# Mi izpišemo agregatno stanje.

fahr = int(input('Vpiši temperaturo vode:'))
celz = (fahr - 32) * (5/9)

# Odločanje o agregatnem stanju
if celz > 100:
    print('Para.')
    print('Plinastno stanje.')
    print('Pazi, da se opečeš.')
elif celz < 0:
    print('Led')
    print('Trdno stanje.')
else:
    print('Voda.')
    print('Tekočina.')

print('Temperatura vode je', celz, '°C.')