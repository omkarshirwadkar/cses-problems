n = int(input())
MODULO = 1000000007
def binExpo(base, expo):
    ans = 1
    while expo:
        if expo & 1:
            ans = (ans * base) % MODULO
        base = (base * base) % MODULO
        expo >>= 1
    return ans
print(binExpo(2, n))