def missing_number(N_array):
    N_array.append(1)
    len_array = len(N_array)

    for i in range(len_array-1):
        N_array[N_array[i]-1]  = -1
    
    for i in range(len_array):
        if N_array[i]>0:
            return i+1
    
print(missing_number([1,2,4]))
