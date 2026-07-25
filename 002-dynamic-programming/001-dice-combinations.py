'''
Count number of ways to construct sum "n" by throwing a dice
We can get the sum as k from the following cases:
i.  add 1 to (k - 1)
ii. add 2 to (k - 2)
...
vi. add 6 to (k - 6)

What is the intuition:
"k" is a very big problem to solve so in order to solve k, 
we say we can get this value of k from the above cases


################################### IMPORTANT #########################################
************************** STATE ****************************

dp[k] = num of ways to get a sum of k


************************ TRANSITION ***************************

dp[k] = sum(dp[k - i], i => 1 to 6, k - i >= 0)


************************* BASE CASE *****************************

dp[0] = 1 ==> Number of ways to get sum 0 is to not roll any dice


*********************** FINAL PROBLEM *************************

dp[n] = num of ways to get sum of n


#####################################################################################
This problem can be solved in reverse as well
Where our state is number of ways to reach n from k
dp[k] = sum(dp[k + i], i => 1 to 6, k + i <= n)

'''


n = int(input())
dp = [0] * (n + 1)
dp[0] = 1
MOD = 1000000007
for i in range(1, n + 1):
    for j in range(1, 7):
        if i >= j:
            dp[i] = (dp[i] + dp[i - j]) % MOD
print(dp[n])