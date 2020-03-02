def triplet(arr):
    n= len(arr)
    for i in range(0,n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                x = arr[i] * arr[i] 
                y = arr[j] * arr[j]
                z = arr[k] * arr[k]
                if (x == y + z) or ( y == z + x) or ( z == x + y):
                    return True

print(triplet([1,2,3,4,5,6]))
