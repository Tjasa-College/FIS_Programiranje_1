imena = ['Ivo', 'Timotej','Maja', 'Rok', 'Aljaž', 'Erika', 'Erna', 'Pia', 'Anže']

# Po abecedi
print(sorted(imena))

# Padajoče po abecedi
print(sorted(imena, reverse=True))

# Soritranje po dolžini imen
print(sorted(imena, key=len))

# Lambda funkcija - enovrstična funkcija
zadnji_znak = lambda niz: niz[-1]
print(sorted(imena, key=zadnji_znak))

# Lambda funkcija je lahko uporabljena neposredno brez imena
print(sorted(imena, key=lambda niz: niz[-1]))
