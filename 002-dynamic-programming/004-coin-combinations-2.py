
n, x = [int(s) for s in input().split()]
c = [int(s) for s in input().split()]
MOD = 1000000007
dp = [[0 for i in range(x + 1)] for j in range(n + 1)]

for i in range(n):
    dp[i][0] = 1

for i in range(n - 1, -1, -1):
    for j in range(1, x + 1):
        skipping = dp[i + 1][j]
        picking = 0
        if c[i] <= j:
            picking = dp[i][j - c[i]]
        dp[i][j] = (skipping + picking) % MOD
print(dp[0][x])