# Izpiši države in imena šahistov s spodnjega seznama

turnir = '''No.		Name	FideID	FED	Rtg
1	GM	Sebenik, Matej	14602296	SLO	2449
2	FM	Pyrih, Roman	14179156	UKR	2378
3	FM	Goroshkov, Maksym	14142716	SLO	2353
4	IM	Soln, Primoz	14601060	SLO	2326
5	IM	Cukrowski, Filip	1171097	POL	2299
6	FM	Stevanic, David	14613921	SLO	2283
7	FM	Kokol, Peter	14604523	SLO	2251
8	IM	Mazi, Leon	14600315	SLO	2246
9	IM	Harshavardhan, G B	25059009	IND	2233
10		Zuzek, Bor	14665590	SLO	2054
11		Mihic, Adam	14655985	SLO	1926
12		Mcghee, Patrick	2407760	SCO	1880
13		Kodela, Marko	14602180	SLO	1821
14		Cerar, Tomaz	14674181	SLO	1548
15		Zakarliuka, Platon	14670887	SLO	1521'''

# Metoda split je definirana nad nizi. Rezultat metode je vedno seznam nizov.
vrstice = turnir.split('\n')

for igralec in vrstice[1:]:
    šahist = igralec.split('\t')[2]
    država = igralec.split('\t')[-2]
    print(država, šahist)