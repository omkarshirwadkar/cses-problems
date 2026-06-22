n = int(input())
multiplier = 0
for i in range(1, n + 1):
    totalSquares = i ** 2
    maxPossible = max(0, ((totalSquares - 1) * totalSquares) // 2)
    multiplier += max(0, (i - 2))
    knightMoves = 8 * multiplier
    print(maxPossible - knightMoves)
# Tehelka analysis
# 0, 0, 8, 24, 48, 80, 120, 168
# 0
# (4 * 3) // 2 = 6 --> 9 --> 0 --> 8 * 0
# (9 * 8) // 2 = 36 --> 28 --> 8 --> 8 * 1
# (16 * 15) // 2 = 120 --> 96 --> 24 --> 8 * 3
# (25 * 24) // 2 = 200 --> 252 --> 48 --> 8 * 6
# (36 * 25) // 2 = 630 --> 550 --> 80 --> 8 * 10
# (49 * 48) // 2 = 1176 --> 1056 --> 120 --> 8 * 15
# (64 * 63) // 2 = 2016 --> 1848 --> 168 --> 8 * 21

