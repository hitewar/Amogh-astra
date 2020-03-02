def findPeakUtil(arr,low,high,n):
    mid = int((low+high) / 2)

    if((mid == 0 or arr[mid-1] <= arr[mid]) and ( mid == n-1 or arr[mid+1] <= arr[mid])):
        print(mid)
    elif((mid>0) and (arr[mid-1]> arr[mid])):
        return findPeakUtil(arr, low, mid-1,n)
    else:
        return findPeakUtil(arr, mid+1, high,n)

arr = [10,20,15,2,23,90,67]
low = 0
high = 6
n = 7
print(findPeakUtil(arr,low,high,n))
