n = int(input())
ans = [n]
while n != 1:
    if n % 2:
        n = (n * 3) + 1
    else:
        n = (n // 2)
    ans.append(n)
print(*ans)