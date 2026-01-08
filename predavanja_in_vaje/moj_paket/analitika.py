import math
def evklidska_razdalja(t1, t2):
    return math.sqrt((t2[0] - t1[0])**2 + (t2[1] - t1[1])**2)

def resi_kvadratno(a, b, c):
    D = math.pow(b, 2) - 4*a*c
    x1 =(-b - math.sqrt(D))/(2*a) if D>=0 else complex(-b,math.sqrt(-D))/(2*a)
    x2 =(-b + math.sqrt(D))/(2*a) if D>=0 else complex(-b,-math.sqrt(-D))/(2*a)
    return x1, x2