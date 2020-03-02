def longestCommonSum(array1, array2,n):
    maxLen = 0
    for i in range(n):

        sum1 = 0
        sum2 = 0
        
        for j in range(i,n):
            sum1 += array1[j]
            sum2 += array2[j]
            print( sum1," ",sum2)            
            if (sum1 == sum2) & ((j-i+1)> maxLen):
                maxLen = (j-i+1)
            else:
                break
        print("\n")
    return maxLen

print(longestCommonSum([0,1,0,1],[0,1,1,0],4))
                
            
