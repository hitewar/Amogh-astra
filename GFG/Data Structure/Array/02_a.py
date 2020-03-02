def union_intersection(arr1 , arr2):
        len1= len(arr1)
        len2= len(arr2)

        union_array = []
        intersection_array = []
        
        i = 0
        j = 0

        while (i < len1) & (j<len2):
            print(str(i)+" "+ str(j)+"\n")
            if arr1[i]<arr2[j]:
                union_array.append(arr1[i])
                i = i + 1
            elif arr1[i] > arr2[j]:
                union_array.append(arr2[j])
                j = j + 1
            else:
                union_array.append(arr1[i])
                intersection_array.append(arr1[i])
                i = i + 1
                j = j + 1

        print(union_array)
        print(intersection_array)

union_intersection([1,2,4,5,6] , [2,3,5,7])



