import sys
def minDistance(arr, x, y):
    distance =  sys.maxsize
    n=len(arr)
    for i in range(n):
        for j in range(i,n):
            if ( ( (arr[i] == x) & ( arr[j] == y) ) | ( (arr[i]==y) & (arr[j]==x) ) ) & (distance > (j - i)):
                distance = j - i

    return distance

print(minDistance([3, 5, 4, 2, 6, 5, 6, 6, 5, 4, 8, 3],3,6))
        
