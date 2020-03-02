def majority(arr):
    n = len(arr)
    for i in arr:
        counter = 0
        for j in arr:
            if i == j:
                counter = counter+1

        if counter >= n/2:
            return i
    return None


print(majority([1,2,3,4,5,1,2,1,1,1,1,1,1,1]))
