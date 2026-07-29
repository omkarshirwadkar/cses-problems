'''
You have one number n, your goal is to make this number 0 by 
subtracting the digits present in it, 
find the minimum number of operations required to achieve this

################################### IMPORTANT #########################################
************************** STATE ****************************

dp[k] = minimum steps to convert "k" to 0


************************ TRANSITION ***************************

dp[k] = 1 + min(dp[k - di], di = ith digit and di != 0)


************************* BASE CASE *****************************

dp[0] = 0 ==> number of steps required to convert 0 to 0


*********************** FINAL PROBLEM *************************

dp[n] = minimum number of steps required to convert n to 0


#####################################################################################

'''
# Greedy Solution: Always take the maximum value and subtract
# n = int(input())
# ans = 0
# m = n
# while m != 0:
#     max_num = int(max(list(str(m))))
#     m -= max_num
#     ans += 1
# print(ans)


n = int(input())
dp = [1000000000] * (n + 1)

dp[0] = 0
for i in range(1, n + 1):
    strn = str(i)
    for j in strn:
        val = int(ord(j) - ord('0'))
        if val != 0:
            dp[i] = min(dp[i], dp[i-val] + 1)
print(dp[n])
