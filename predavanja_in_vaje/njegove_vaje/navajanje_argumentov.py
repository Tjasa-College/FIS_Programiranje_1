def izracunaj_ceno(cena: float, popust: int = 10, ddv: int = 22) -> float:
    cena_popust = cena * (1 - popust/100)
    cena_ddv = cena_popust * (1 + ddv/100)
    return round(cena_ddv, 2)

print(izracunaj_ceno(53.35))
print(izracunaj_ceno(53.35, ddv=9))
print(izracunaj_ceno(53.35, ddv=9, popust=0))
print(izracunaj_ceno(53.35, 15, 22))

'''
print('Ana', 'Bine', 'Polde')
print('Ana', 'Bine', 'Polde', sep='-')
print('Ana', 'Bine', 'Polde', sep='+', end='\n')
print('Ana', 'Bine', 'Polde', end='--->\n\n\n', sep='+')
'''