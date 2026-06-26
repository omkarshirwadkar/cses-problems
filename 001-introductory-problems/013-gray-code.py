n = int(input())
def graycode(n):
    # Base Case
    if n == 1:
        return ["0", "1"]
    # Get the strings for length n - 1
    prevGrayCode = graycode(n - 1)
    # Reverse the previous gray code for length n - 1
    revPrevGrayCode = prevGrayCode[::-1]
    # Append 0 to the previous gray code
    currFirstHalf = ["0" + i for i in prevGrayCode]
    # Append 1 to the reversed previous gray code
    currSecHalf = ["1" + i for i in revPrevGrayCode]
    # Return the answer
    return currFirstHalf + currSecHalf
temp = graycode(n)
for i in range(2**n):
    print(temp[i])