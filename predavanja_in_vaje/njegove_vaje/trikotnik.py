# Uporabnik naj vnese stranico triktnika.
# Mi izpišemo ploščino enakovstračničnega trikotnika.

from math import *

a = float(input('Vpiši dolžino stranice:'))

pl = a ** 2 * sqrt(3) / 4

print('Ploščina trikotnika je', round(pl,2), 'cm.')