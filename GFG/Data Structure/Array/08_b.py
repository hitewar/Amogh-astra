def nextgreatest(arr):
    maxfromright = arr[-1]
    arr[-1] = -1
    n = len(arr)
    for i in range(n-2,-1,-1):
        temp = maxfromright
        if arr[i]>maxfromright:
            maxfromright = arr[i]

        arr[i] = temp
    return arr

print(nextgreatest([16,17,4,3,5,2]))

