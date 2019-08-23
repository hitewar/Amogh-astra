#!/bin/python3

import math
import os

# Complete the solve function below.
def solve(a):
    empty_list =[]
    num_1 = sum([1 if(i==1) else 0 for i in a])
    [a.remove(1) for i in range(num_1)]

    for i in sorted(a):
        index_list=[]
        for m in empty_list:
            for n in m:
                if math.gcd(i,n)!=1:
                    index_list.append(m)
                    break
        if len(index_list)==0:
            empty_list.append([i])
        else:
            temp =[] 
            for j in index_list:
                temp = temp + j
            temp.append(i)
            empty_list[empty_list.index(index_list[0])] = sorted(temp)
            for k in index_list[1:]:
                empty_list.remove(k)
    if (num_1+len(empty_list))==1:
        return 0
    else:
        return int((math.pow(2,num_1+len(empty_list)))%(math.pow(10,9)+ 7)) -2

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        a_count = int(input().strip())

        a = list(map(int, input().rstrip().split()))
        result = solve(a)
        fptr.write(str(result) + '\n')

    fptr.close()
