'''
You have an array of coins consisting "n" different coins
Your task is to find the number of ways to get a sum of "x"

################################### IMPORTANT #########################################
************************** STATE ****************************

dp[k] = number of ways to construct a sum of k


************************ TRANSITION ***************************

dp[k] = sum(dp[k - ci], i => 1 to n, k - ci >= 0)


************************* BASE CASE *****************************

dp[0] = 1 ==> The sum 0 can be constructed in only 1 way, not chosing anyting


*********************** FINAL PROBLEM *************************

dp[x] = number of ways to calculate a sum of x


#####################################################################################

'''
n, x = [int(v) for v in input().split()]
c = [int(v) for v in input().split()]

dp = [0] * (x + 1)
dp[0] = 1
MOD = 1000000007

# OPTIMIZATION: Loop through coins FIRST (Outer Loop)
# This prevents checking unavailable coins repeatedly

for coin in c:
    for i in range(coin, x + 1):
            dp[i] = (dp[i - coin] + dp[i]) % MOD 
print(dp[x])