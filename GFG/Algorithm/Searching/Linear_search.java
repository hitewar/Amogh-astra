/******************************************************************************
Problem: Given an array arr[] of n elements, write a function to search a given element x in arr[].
*******************************************************************************/
public class Main
{
	public static void main(String[] args) {
	    int[] A = new int[]{1,2,3,4,5,6,7,8,9,20};
	    int search_num= 8,i;
	    for(i=0;i<A.length;i++){
	       if(search_num == A[i]){
	           System.out.println("The value "+ search_num+" is at index: "+i);
	           break;
	       }
	    }
	    if(i==A.length){
	        System.out.println("The given value is Invalid");
	    }
	}
}
