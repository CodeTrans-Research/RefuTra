import sys
import math
import heapq
from queue import Queue
import numpy as np
# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( arr , n ) :
    brr = [ 0 ] * ( 2 * n + 1 )
    for i in range ( n ) :
        brr [ i ] = arr [ i ]
    for i in range ( n ) :
        brr [ n + i ] = arr [ i ]
    maxHam = 0
    for i in range ( 1 , n ) :
        currHam = 0
        k = 0
        for j in range ( i , i + n ) :
            if brr [ j ] != arr [ k ] :
                currHam += 1
                k = k + 1
        if currHam == n :
            return n
        maxHam = max ( maxHam , currHam )
    return maxHam


def f_filled(arr, n):
    brr = [0] * (2*n + 1)
    
    for i in range(n):
        brr[i] = arr[i]
    
    for i in range(n):
        brr[n + i] = arr[i]
        
    maxHam = 0
    
    for i in range(1, n):
        currHam = 0
        for j in range(i, i + n):
            if brr[j] != arr[j - i]:
                currHam += 1
        if currHam == n:
            return n
        maxHam = max(maxHam, currHam)
    
    return maxHam

if __name__ == '__main__':
    param = [
    ([1, 4, 18, 22, 28, 34, 35, 39, 44, 45, 67, 73, 75, 79, 81, 83, 89, 93, 96],12,),
    ([52, -28],1,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],21,),
    ([24],0,),
    ([-68, 14, 36, 62],2,),
    ([1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0],12,),
    ([7, 10, 19, 22, 24, 28, 29, 39, 46, 55, 62, 66, 68, 73, 74, 76, 83, 84, 85, 99],15,),
    ([-38, 56, 86, 12, 24, -90, -20, -46, 38, 92, -44, -74, 54, 50, 46, 50, -94, 64, 32, -84, 70],14,),
    ([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],8,),
    ([61, 89, 8],2,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        import copy
        p2 = copy.deepcopy(parameters_set)
        filledres = f_filled(*parameters_set)
        goldres = f_gold(*p2)
        if filledres == goldres:
            n_success+=1
        else:
            if set([filledres,goldres]) <= set([float("inf"),sys.maxsize,2147483647]) or set([filledres,goldres]) <= set([float("-inf"),-sys.maxsize-1,-sys.maxsize,-2147483648]):
                n_success += 1
    print("#Results: %i, %i" % (n_success, len(param)))
