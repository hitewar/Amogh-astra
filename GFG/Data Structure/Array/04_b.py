import sys
def minDistance(arr, x, y):
    min_length = sys.maxsize
    prev_index = -1

    for i in range(len(arr)):
        if (arr[i] == x ) | (arr[i] == y):
            if prev_index != -1:
                if arr[prev_index] != arr[i]:
                    if min_length > abs(prev_index - i):
                        min_length = abs(prev_index - i)
                                
                prev_index = i
            else:
                prev_index = i        
        print(arr[i], prev_index)
    return min_length

print(minDistance([3, 5, 4, 2, 6, 5, 6, 5, 4, 8, 3],3,6))





