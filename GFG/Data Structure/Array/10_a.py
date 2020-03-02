def peak_element(arr):
    if len(arr)==1:
        print(arr[0])
        return 

    if arr[0]>= arr[1]:
        print(arr[-1])

    for i in range(1,len(arr)-1):
        if (arr[i]>= arr[i-1]) & (arr[i]>= arr[i+1]):
            print(arr[i])

    if arr[-1] >= arr[-2]:
        print(arr[-1])

#peak_element([5,10,20,15])
peak_element([10,20,15,2,23,90,67])
