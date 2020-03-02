def leaders(arr):
    n = len(arr)
    max_from_right = [] 
    max_element = arr[len(arr) - 1]
    for i in range(0,n):
        if arr[n-i-1]>=max_element:
            max_element = arr[n-i-1]
            max_from_right = [arr[n-i-1]] + max_from_right
    print(max_from_right)


leaders([16,17,4,3,5,2])

