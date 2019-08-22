#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(board):
    length = len(board)
    first_value=board[0][0]
    for i in range(length):
        for j in range(length):
            #even-odd position
            if ((i%2==0)+(j%2==0))%2==1:
                if board[i][j]!=(first_value+1)%2:
                    return 'No'
            else:#even-even / odd-odd position 
                if board[i][j]!=(first_value)%2:
                    return 'No'

    return 'Yes'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        board = []
        for _ in range(n):
            board.append(list(map(int, input().rstrip().split())))

        result = solve(board)
        fptr.write(result + '\n')
    fptr.close()
