import math
import trikot

def pravokotnik(a, b):
    p = a * b
    return p


def kvadrat(a):
    p = a ** 2
    return p


def krog(r):
    p = math.pi * (r ** 2)
    return p


def trikotnik(vrsta, *args):
    #enakostranični, pravokotni, enakokratni, splošni
    if not isinstance(vrsta, str):
        raise ValueError("Parameter 'vrsta' mora biti niz (string).")

    v = vrsta.strip().lower()

    if v == "enakostranicni":
        if len(args) != 1:
            raise ValueError("Za enakostranični trikotnik podaš 1 parameter: (a).")
        return trikot.enakostranicni(args[0])

    if v == "pravokotni":
        if len(args) != 2:
            raise ValueError("Za pravokotni trikotnik podaš 2 parametra: (a, b).")
        return trikot.pravokotni(args[0], args[1])

    if v == "enakokraki":
        if len(args) != 2:
            raise ValueError("Za enakokraki trikotnik podaš 2 parametra: (a, c).")
        return trikot.enakokraki(args[0], args[1])

    if v == "splosni":
        if len(args) != 3:
            raise ValueError("Za splošni trikotnik podaš 3 parametre: (a, b, c).")
        return trikot.splosni(args[0], args[1], args[2])

    raise ValueError(f"Neznana vrsta trikotnika: '{vrsta}'.")


