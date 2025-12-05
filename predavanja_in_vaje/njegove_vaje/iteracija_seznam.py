# Izpiši poštevanko od 1 do 10 za poljubno število

# Ročno kreiranje številčnega seznama.
ponovitve = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
štev = int('Vpiši število za poštevanko:')

for pon in ponovitve:
    # pon = ponovitve[i], i=1, 2, 3, ..
    print(f'{štev} * {pon} = {štev * pon}')

# Kreiranje seznama pred zanko.
nums = list(range(1,11))
for num in nums:
    print(f'{štev} * {num} = {štev * num}')

# Kreiranje seznama v glavi zanke.
for num in list(range(1,11)):
    print(f'{štev} * {num} = {štev * num}')

# Pretvorba v seznam dejansko ni potrebna.
for num in range(1,11):
    print(f'{štev} * {num} = {štev * num}')
