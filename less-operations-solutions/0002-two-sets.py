n = int(input())
totalSum = ((n + 1) * n) // 2
if totalSum % 2:
    print("NO")
else:
    arr1 = []
    arr2 = []
    midSum = totalSum // 2
    for i in range(n, 0, -1):
        if midSum >= i:
            arr1.append(i)
            midSum -= i
        else:
            arr2.append(i)
    print("YES")
    print(len(arr1))
    print(*arr1)
    print(len(arr2))
    print(*arr2)