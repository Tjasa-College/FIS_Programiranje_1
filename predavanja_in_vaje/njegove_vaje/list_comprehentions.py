# Seznam kvadratov števil od 1 do 10.
kvadrati = [x ** 2 for x in range(1,11)]
print(kvadrati)

# Potence števila 2 do 10.
p2 = [2 ** n for n in range(1,11)]
print(p2)

# Seznam števil od 1 do 30, ki so deljiva s 3 in ne z 2.
nums = [x for x in range(1,31) if x % 3 == 0 and x % 2 != 0]
print(nums)

# Terka števil od 1 do 30, ki so deljiva s 3 in ne z 2.
tnums = tuple(x for x in range(1,31) if x % 3 == 0 and x % 2 != 0)
print(tnums)

# Izdelaj seznam 10 decimalnih števil na intervalu od 0 do 1, ki
# so med seboj enako oddaljena tj. 0.0, 0.1, 0.2, ...
dec_nums = [x/10 for x in range(0,11)]
print(dec_nums)

# Izdealjmo matriko parov v velikosti 5 x 5.
matrika = [[(i,j) for i in range(1,6)] for j in range(1,6)]
print(matrika)

# Izdealjmo kooridante šahovnice.
chess_board = [[(s,v) for s in 'ABCDEFGH'] for v in range(1,9)]
print(chess_board)

# Izdealjmo kooridante šahovnice.
šahovnica = [[s+v for s in 'ABCDEFGH'] for v in '12345678']
print(šahovnica)
