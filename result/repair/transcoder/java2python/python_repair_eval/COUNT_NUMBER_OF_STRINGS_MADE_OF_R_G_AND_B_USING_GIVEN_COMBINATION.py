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
def f_gold ( n , r , b , g ) :
    fact = [ 0 for i in range ( n + 1 ) ]
    fact [ 0 ] = 1
    for i in range ( 1 , n + 1 , 1 ) :
        fact [ i ] = fact [ i - 1 ] + i
    left = n - ( r + g + b )
    sum = 0
    for i in range ( 0 , left + 1 , 1 ) :
        for j in range ( 0 , left - i + 1 , 1 ) :
            k = left - ( i + j )
            sum = int ( sum + fact [ n ] / ( fact [ i + r ] + fact [ j + b ] + fact [ k + g ] ) )
    return sum


def f_filled ( n , r , b , g ) :
    fact = (n + 1) * [0]
    for i in range ( 1 , n + 1 ) :
        fact [ i ] = fact [ i - 1 ] + i
    left = n - ( r + g + b )
    sum = 0
    for i in range ( 0 , left + 1 ) :
        for j in range ( 0 , left - i + 1 ) :
            k = left - ( i + j )
            sum =  sum+fact[n]//(fact[i+r]+fact[j+b]+fact[k+g])
    return sum

if __name__ == '__main__':
    param = [
    (90,75,22,66,),
    (32,65,5,46,),
    (94,17,44,2,),
    (50,23,92,49,),
    (16,10,72,71,),
    (37,91,7,9,),
    (75,97,38,69,),
    (88,51,32,79,),
    (27,4,20,17,),
    (67,99,53,70,)
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
