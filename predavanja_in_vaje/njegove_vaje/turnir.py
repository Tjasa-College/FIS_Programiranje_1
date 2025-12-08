turnir = '''No.		Name	FideID	FED	Rtg	Club/City
1	II	Gabrijan, Timotej	14624559	SLO	2127	ŠD FRAM
2	I	Velec, Jože	14606844	SLO	2030	ŠD FRAM
3	II	Štern, Urban	14625148	SLO	1984	Celjski ŠK
4	II	Kancler, Uroš		SLO	1850	
5	III	Brezner, Franci	14640171	SLO	1678	ŠD FRAM
6		Badrov, Gal	14631180	SLO	1645	ŠD FRAM
7		Mom, Rado		SLO	1521	ŠD FRAM
8		Mejal, Gorazd		SLO	1502	ŠD FRAM
9		Božič, Jure	14659590	SLO	1000	ŠD FRAM
10		Hostej, Bron	14659603	SLO	1000	ŠD FRAM
11		Kancler, Amadej	14671948	SLO	1000	ŠD FRAM
12		Rozman, Maksim	14652595	SLO	1000	ŠD FRAM
'''

# Ob uporabi metode split nad str dobim seznam nizov.
vrstice = turnir.split('\n')

# Šahisti so vse vrstice razen glave tabele.
šahisti = vrstice[1:]

for igralec in šahisti:
    print(igralec.split('\t'))