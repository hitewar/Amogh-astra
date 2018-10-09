/******************************************************************************
Problem: Given an array arr[] of n elements, write a function to search a given element x in arr[].
*******************************************************************************/
#include <stdio.h>

int search(int A[],int n,int x){
    for(int i=0;i<n;i++)
        if(A[i]==x)
        return i;
        
        return -1;
}

int main()
{int A[10]={1,2,3,4,5,6,7,8,9,20};
 int num_to_check=11,i=0;
 for(i=0;i<10;i++){
     if(A[i]==num_to_check){
         printf("The number %d is at index: %d",A[i],i);
         break;
     }
 }
 if(i==10){
     printf("The number not found!!");
 }
 
 printf("%d",search(A,10,20));
}
