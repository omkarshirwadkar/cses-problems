n = int(input())
arr = [int(x) for x in input().split()]
sumArr = sum(arr)
totalSum = ((n + 1) * n) // 2
print(totalSum - sumArr)