s = input()
n = len(s)
charCountMap = {}
for i in range(n):
    if s[i] in charCountMap:
        charCountMap[s[i]] += 1
    else:
        charCountMap[s[i]] = 1
totalOdds = 0
for i in charCountMap.values():
    if i & 1:
        totalOdds += 1
if totalOdds > 1:
    print("NO SOLUTION")
else:
    arr = []
    oddChar = []
    for i, j in charCountMap.items():
        if j & 1:
            oddChar.extend([i] * j)
        else:
            arr.extend([i] * (j // 2))
    ans = arr + oddChar + arr[::-1]
    print("".join(ans))