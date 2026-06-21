s = input()
ans = 1
curr = 1
n = len(s)
for i in range(n - 1):
    if s[i] == s[i + 1]:
        curr += 1
        ans = max(ans, curr)
    else:
        curr = 1
print(ans)