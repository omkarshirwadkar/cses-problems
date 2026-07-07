n = int(input())
MODULO = 1000000007
def binaryExponent(base, expo):
    # Initializing the answer
    ans = 1
    while expo:
        # If exponent value is odd then we multiply 1 times the base to the answer, 
        # This makes the exponent value even, 
        # As the value is even we can square the base and reduce the power by half
        if expo & 1:
            ans = (ans * base) % MODULO
        base = (base * base) % MODULO
        # This operation is just dividing by 2 when expo is even
        expo >>= 1
    return ans
print(binaryExponent(2, n))