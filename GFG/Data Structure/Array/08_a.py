def next_greatest(arr):
    n = len(arr)
    for i in range(n-2,-1,-1):
        temp = arr[i+1]
        for j in range(i+1,n):           
            if arr[j] > temp:
                temp = arr[j]
        arr[i+1] = temp
    return arr[1:]+[-1]

print( next_greatest([16,17,4,3,5,2]))
