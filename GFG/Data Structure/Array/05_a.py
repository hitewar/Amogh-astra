def leaders(arr):
    n = len(arr)
    for i in range(0,n):
        cursor = 0        
        for j in range(i,n):
            if arr[i]>=arr[j]:
                cursor = cursor + 1
        if cursor == (n-i):
            print(arr[i])

leaders([16,17,4,3,5,2])





