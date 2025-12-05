# Program ugotovi status VIP kupca
# Skupaj nakupi > 1000 EUR
# ALI
# Več kot 9 nakupov

skupaj = float(input('Vnesi znesek nakupov:'))
st_nakupov = int(input('Vnesi šzevilo nakupov:'))

vip = skupaj > 1000 or st_nakupov > 9

if vip:
    print('Imaš VIP status.')
else:
    print('Nisi še VIP kupec.')

