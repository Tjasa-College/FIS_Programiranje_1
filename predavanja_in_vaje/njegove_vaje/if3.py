# VIP kupec
# Skupaj za več kot 800 € nakupov v letu.
# Ali vsaj 10 nakupov nad 50 €.

nakupi = float(input('Znesek vseh nakupov:'))
st_nad_50 = int(input('Ševilo nakupov nad 50 €:'))

vip = nakupi > 800 or st_nad_50 > 10

if vip:
    print('Si že VIP kupec.')
else:
    print('Nisi še VIP kupec.')