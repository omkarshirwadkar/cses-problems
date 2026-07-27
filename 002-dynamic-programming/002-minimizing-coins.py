'''
You have an array of coins consisting "n" different coins
Your task is to use minimum number of any combination of coins and get a sum of "x"

################################### IMPORTANT #########################################
************************** STATE ****************************

dp[k] = minimum number of coins required to construct a sum of k


************************ TRANSITION ***************************

dp[k] = 1 + min(dp[k - ci], i => 1 to n, k - ci >= 0)


************************* BASE CASE *****************************

dp[0] = 0 ==> In order to construct a sum of 0 you need 0 coins


*********************** FINAL PROBLEM *************************

dp[x] = minimum number of coins required to construct a sum of x


#####################################################################################

'''
n, x = [int(s) for s in input().split()]
c = [int(s) for s in input().split()]
INF = 10**9
dp = [INF] * (x + 1)
dp[0] = 0

for i in range(1, x + 1):
    for coin in c:
        if i >= coin:
            dp[i] = min(dp[i], dp[i - coin] + 1)

print(dp[x] if dp[x] < INF else -1)