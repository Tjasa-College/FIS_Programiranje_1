import math

def enakostranicni(a):
    s = 3 * a / 2
    pl= (1/4)*math.sqrt(s*(s-a)*(s-a)*(s-a))
    return pl

def pravokotni(a, b):
    pl = (a * b) /2
    return pl

def enakokraki(a, c):
    s = (2 * a + c)/ 2
    pl = (1 / 4) * math.sqrt(s * (s - a) * (s - a) * (s - c))
    return pl

def splosni(a, b, c):
    s = (a + b + c) / 2
    pl = (1 / 4) * math.sqrt(s * (s - a) * (s - b) * (s - c))
    return pl