t = int(input())
for _ in range(t):
    x, y = [int(s) for s in input().split()]
    if y >= x:
        if y % 2:
            print((y ** 2) - (x - 1))
        else:
            print(((y - 1) ** 2) + x)
    else:
        if x % 2:
            print(((x - 1) ** 2) + y)
        else:
            print((x ** 2) - (y - 1))