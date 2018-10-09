
'''******************************************************************************
Problem: Given an array arr[] of n elements, write a function to search a given element x in arr[].
*******************************************************************************'''
def search(A,n,x):
    for i in range(n):
        if A[i]==x:
            return i
    return -1
    
def main():
    A=[1,2,3,4,5,6,7,8,9,20]
    x=30
    print("The value lies at index: ",search(A,len(A),x)) if search(A,len(A),x)!=-1 else print("The value not found")
    return 0
    
main()
