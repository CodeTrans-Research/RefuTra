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
def f_gold ( n , k ) :
    dp = [ [ [ 0 , 0 ] for __ in range ( k + 1 ) ] for _ in range ( n + 1 ) ]
    dp [ 1 ] [ 0 ] [ 0 ] = 1
    dp [ 1 ] [ 0 ] [ 1 ] = 1
    for i in range ( 2 , n + 1 ) :
        for j in range ( k + 1 ) :
            if j >= i:
                break
            else:
                dp [ i ] [ j ] [ 0 ] = ( dp [ i - 1 ] [ j ] [ 0 ] + dp [ i - 1 ] [ j ] [ 1 ] )
                dp [ i ] [ j ] [ 1 ] = dp [ i - 1 ] [ j ] [ 0 ]
                if j >= 1 :
                    dp [ i ] [ j ] [ 1 ] += dp [ i - 1 ] [ j - 1 ] [ 1 ]
    return dp [ n ] [ k ] [ 0 ] + dp [ n ] [ k ] [ 1 ]


def f_filled ( n , k ) :
    dp = [[[0 for _ in range(2)] for _ in range(k+1)] for _ in range(n+1)]
    dp [ 1 ] [ 0 ] [ 0 ] = 1
    dp [ 1 ] [ 0 ] [ 1 ] = 1
    for i in range ( 2 , n + 1 ) :
        j=0 
        while j<i and j<k+1 :
            dp [ i ] [ j ] [ 0 ] = dp [ i - 1 ] [ j ] [ 0 ] + dp [ i - 1 ] [ j ] [ 1 ]
            dp [ i ] [ j ] [ 1 ] = dp [ i - 1 ] [ j ] [ 0 ]
            if j - 1 >= 0 :
                dp [ i ] [ j ] [ 1 ] += dp [ i - 1 ] [ j - 1 ] [ 1 ]
            j += 1
    return dp [ n ] [ k ] [ 0 ] + dp [ n ] [ k ] [ 1 ]

if __name__ == '__main__':
    param = [
    (29,85,),
    (47,29,),
    (77,96,),
    (9,91,),
    (29,80,),
    (94,85,),
    (51,87,),
    (46,62,),
    (18,96,),
    (86,86,)
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
