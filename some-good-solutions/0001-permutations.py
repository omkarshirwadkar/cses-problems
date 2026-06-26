# The problem is to print a permutation of n such that
# the difference between the adjacent elemets is not equal to 1
n = int(input())
if n == 1:
    print(1)
elif n < 4:
    print("NO SOLUTION")
else:
    print(*range(2, n + 1, 2), *range(1, n + 1, 2))