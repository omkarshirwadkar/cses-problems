n = int(input())
def graycode(n):
    # Base Case
    if n == 1:
        return ["0", "1"]
    # Calculate the strings for length n - 1
    prevGrayCode = graycode(n - 1)
    # Reverse the previous Gray Code for length n - 1
    reversedPrevGrayCode = prevGrayCode[::-1]
    prevSize = len(prevGrayCode)
    index = 0
    while index < prevSize:
        # Prepend the character "1" in previous gray codes
        appendOne = "1" + prevGrayCode[index]
        # Prepend the character "0" in reversed previous gray codes
        prevGrayCode[index] = "0" + reversedPrevGrayCode[index]
        prevGrayCode.append(appendOne)
        index += 1
    return prevGrayCode
temp = graycode(n)
for i in range(2**n):
    print(temp[i])