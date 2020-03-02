def countIncreasing(arr):
    n = len(arr)
    count = 0

    for i in range(0,n):
        for j in range(i+1,n):
            if arr[j]>arr[j-1]:
                count = count + 1
            else:
                break
    return count

print(countIncreasing([1,2,2,4]))
    
