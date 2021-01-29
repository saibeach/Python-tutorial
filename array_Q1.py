def getMaxLength(arr, n):
    #initialize count
    count = 0

    #initialize max
    result = 0

    for i in range(0,n):
        if (arr[i] == 0):
            count = 0

        else:
            count += 1
            result = max(result, count)
    return result


arr = [1,1,1,0,1,0,1,1,1,1,0,0,0,0,1,0,1,0,1]

n = len(arr)

print(getMaxLength(arr,n))
