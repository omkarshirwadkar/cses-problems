'''
You have an array of coins consisting "n" different coins
Your task is to find the number of "distinct ordered ways" you can 
produce a money sum "x" using the available coins

** Pick -- Not Pick condition

C1 C2 C3 C4 C5
--> C1 + C1 + C2 + C2 + C5 = x
--> C1 + C2 + C1 + C2 + C5 = x
--> C2 + C2 + C1 + C1 + C5 = x
How to make sure that the above cases are counted only as once?

----> All the Ci < Ci+1

Coins: C1 ----------- Cn

                                        X
                                        /\
                                       /  \
                                      /    \
                                     /      \
                                C1, X-C1   C2, X-C2


There are 2 Important Things to solve this problem:
1. What is the integer that you want to construct as a sum
2. What are the coins that you can actually pick up


                                P --> (i, k)
                                        /\
                                  Pick / \\ Not Pick
                                      /    \
                              P1     /     \\  P2
                             (i, k - ci)   (i + 1, k)
                        Constructing       Constructing
                        a smaller sum    using smaller set


If you want to construct a sum of 0
It doesn't matter how many coins you have left
The number of ways are going to be just 1
You will not be picking up any of the coins
################################### IMPORTANT #########################################
************************** STATE ****************************

dp[i][k] = no of ways to get a sum of k such that 
all coins from Ci to Cn are pickable 
and all coins before Ci are skipped


************************ TRANSITION ***************************
            |====> dp[i + 1][k] skip coin i move to next
dp[i][k] == |           +
            |====> dp[i][k - Ci] pick coin i


************************* BASE CASE *****************************

dp[i][0] = 1 ==> The sum 0 can be constructed by not chosing anyting


*********************** FINAL PROBLEM *************************

dp[1][x] = no. of ways to get a sum of x such that 
all coins from C1 to Cn are pickable 


#####################################################################################

'''
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