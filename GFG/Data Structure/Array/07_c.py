def findoddoccurrance(arr):
    result = arr[0]
    for i in arr[1:]:
        result = result ^ i

    return result

print(findoddoccurrance([1,2,3,1,2,4,4]))
