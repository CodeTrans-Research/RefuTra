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
def f_gold ( A ) :
    n = 2 * A
    dpArray = [ 0 ] * ( n + 1 )
    dpArray [ 0 ] = 1
    dpArray [ 2 ] = 1
    for i in range ( 4 , n + 1 , 2 ) :
        for j in range ( 0 , i - 1 , 2 ) :
            dpArray [ i ] += ( dpArray [ j ] * dpArray [ i - 2 - j ] )
    return int ( dpArray [ n ] )


def f_filled ( A ) :
    n = 2 * A
    dpArray = [0 for _ in range(n+1)]
    dpArray [ 0 ] = 1
    dpArray [ 2 ] = 1
    for i in range ( 4 , n + 1 , 2 ) :
        for j in range ( 0 , i - 1 , 2 ) :
            dpArray [ i ] += ( dpArray [ j ] * dpArray [ i - 2 - j ] )
    return dpArray [ n ]

if __name__ == '__main__':
    param = [
    (32,),
    (52,),
    (52,),
    (32,),
    (73,),
    (31,),
    (29,),
    (75,),
    (39,),
    (49,)
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
