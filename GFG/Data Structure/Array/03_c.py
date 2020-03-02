def missing_number(arr):
    x1 = arr[0]
    x2 = 1
    for i in arr[1:]:
        x1 = x1 ^ i
    for i in range(1,len(arr) + 1):
        x2 = x2 ^ (i+1)

    return x1 ^ x2

print(missing_number([1,2,4]))
