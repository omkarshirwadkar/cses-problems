t = int(input())
for _ in range(t):
    a, b = [int(s) for s in input().split()]
    conditionOne = ((a + b) % 3) == 0
    conditionTwo = max(a, b) <= (2 * min(a, b))
    if conditionOne and conditionTwo:
        print("YES")
    else:
        print("NO")