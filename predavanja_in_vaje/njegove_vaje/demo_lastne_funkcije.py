# Funkcija, ki pretvarja °F v °C.
def fahr2celz(fahr):
    celz = (fahr - 32) * (5/9)
    return celz

# Prazna oz. še nerealizirana funkcija (prazen stavek pass).
def datum_roj(emso):
    pass

# Prazna oz. še nerealizirana funkcija (elipsis operator kot prazen stavek).
def spol(emso):
    ...

# Elipsis lahko dodaš tudi kar za dvopičjem.
def prototip_funkcije(): ...

# Funkcija, ki ničesar ne vrača. Le izpiše nekaj.
def pozdrav():
    print('Pozdravljen.')
    print('Sem na predavnju o Pythonu')

odziv = pozdrav()

print(odziv)
print('datum_roj -->',datum_roj('1008967500164'))
print('spol -->',spol('1008967500164'))
print('100°F = ',fahr2celz(100), '°C')