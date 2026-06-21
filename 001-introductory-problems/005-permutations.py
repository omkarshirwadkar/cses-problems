n = int(input())
if n < 4:
    if n == 1:
        print(1)
    else:
        print("NO SOLUTION")
elif n > 4:
    ans = [0] * n
    j = 1
    for i in range(0, n, 2):
        ans[i] = j
        j += 1
    for i in range(1, n, 2):
        ans[i] = j
        j += 1
    print(*ans)
else:
    ans = [2, 4, 1, 3]
    print(*ans)