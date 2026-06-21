n = int(input())
a = [int(x) for x in input().split()]
ans = 0
for i in range(n - 1):
    temp = max(0, a[i] - a[i + 1])
    ans += temp
    a[i + 1] += temp
print(ans)