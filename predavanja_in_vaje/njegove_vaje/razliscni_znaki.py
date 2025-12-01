# Uporabnik vnese besedilo.
# Program izpiše samo različne znake. Noben znak ne sme biti izpisan dvakrat.

unikatni = ''
besedilo = input('Vnesi besedilo:')

for znak in besedilo:
    if znak not in unikatni:
        unikatni += znak

print('Zanki v besedilu:', unikatni)
print(f'V besedilu je {len(unikatni)} različnih znakov.')