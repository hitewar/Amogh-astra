def fixed_point(arr):
    result = -1
    for i in range(0,len(arr)):
        if i == arr[i]:
            result = i
            break

    return result

print(fixed_point([1,2,3,4,5,5]))
