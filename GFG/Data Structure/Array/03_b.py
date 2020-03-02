def missing_number(N_array):
    return int( (( (len(N_array)+2) * (len(N_array)+1))/2 ) - sum(N_array))

print(missing_number([1,2,4,5]))
