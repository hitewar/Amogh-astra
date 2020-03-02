def countIncreasing(arr):
    n = len(arr)
    sa_len = 1
    count = 0

    for i in range(0,n-1):
        if arr[i+1]>arr[i]:
            sa_len = sa_len + 1
        else:
            count = count + (sa_len * (sa_len-1))/2
            sa_len = 1

    if sa_len > 1:
        count = count +(sa_len * ( sa_len-1))/2

    return count

print(countIncreasing([1,2,3,4,4,5]))
