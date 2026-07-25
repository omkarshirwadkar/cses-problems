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
import sys
def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    x = int(data[1])
    c = [int(v) for v in data[2:2+n]]
    
    INF = 10**9
    dp = [INF] * (x + 1)
    dp[0] = 0
    
    # OPTIMIZATION: Loop through coins FIRST (Outer Loop)
    # This prevents checking unavailable coins repeatedly
    for coin in c:
        for i in range(coin, x + 1):
            new_val = dp[i - coin] + 1
            if new_val < dp[i]:
                dp[i] = new_val
                
    print(dp[x] if dp[x] < INF else -1)

if __name__ == '__main__':
    main()
