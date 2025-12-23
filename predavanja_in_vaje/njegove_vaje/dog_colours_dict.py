# Breed,Country of Origin,Fur Color,Height (in),Color of Eyes,Longevity (yrs),Character Traits,Common Health Problems
# Labrador Retriever,Canada,"Yellow, Black, Chocolate",21-24,Brown,10-12,"Loyal, friendly, intelligent, energetic, good-natured","Hip dysplasia, obesity, ear infections"
# Izpis množice vseh različnih barv

import csv

barve = set()
with open('dog_breeds.csv') as datoteka:
    vsebina = csv.DictReader(datoteka)
    #print(type(vsebina))
    #print(list(vsebina))
    for vrstica in vsebina:
        barve |= set(vrstica['Fur Color'].split(','))

    print(sorted(barve))
    barve = sorted(barve)
    barve = [barva.strip() for barva in barve]

    print(barve)