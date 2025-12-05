# Izpišimo seznam pretvorb temperatur od -50 do +100°F v °C s korakom 10.

for fahr in range(-50,101,10):
    celz = (fahr - 32) * 5 / 9
    print(f'{fahr}°F = {celz:.2f}°C')