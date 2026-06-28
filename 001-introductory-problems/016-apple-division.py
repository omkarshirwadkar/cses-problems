def appleDivision(idx, arr, sum1, sum2, n):
    # End is reached, return the difference between the two sums
    if idx == n:
        return abs(sum1 - sum2)
    
    # Add the current apple(at idx) to group 1
    take = appleDivision(idx + 1, arr, sum1 + arr[idx], sum2, n)

    # Add the current apple(at idx) to group 2
    notTake = appleDivision(idx + 1, arr, sum1, sum2 + arr[idx], n)
    
    # Return the minimum of both the choices
    return min(take, notTake)

n = int(input())
arr = [int(x) for x in input().split()]
print(appleDivision(0, arr, 0, 0, n))