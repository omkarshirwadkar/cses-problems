n = int(input())
totalSum = ((n + 1) * n) // 2
if totalSum % 2:
    print("NO")
else:
    arr1 = []
    arr2 = []
    if n % 2:
        arr1.extend([1,2])
        arr2.append(3)
        for i in range(4, n + 1, 4):
            arr1.extend([i, i + 3])
            arr2.extend([i + 1, i + 2])
    else:
        for i in range(1, n + 1, 4):
            arr1.extend([i, i + 3])
            arr2.extend([i + 1, i + 2])
    print("YES")
    print(len(arr1))
    print(*arr1)
    print(len(arr2))
    print(*arr2)