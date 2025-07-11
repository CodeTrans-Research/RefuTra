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
def f_gold ( n , r , p ) :
    C = [ 0 for i in range ( r + 1 ) ]
    C [ 0 ] = 1
    for i in range ( 1 , n + 1 ) :
        for j in range ( min ( i , r ) , 0 , - 1 ) :
            C [ j ] = ( C [ j ] + C [ j - 1 ] ) % p
    return C [ r ]


def f_filled ( n , r , p ) :
    C = np.zeros ( ( r + 1 , ) )
    C [ 0 ] = 1
    for i in range ( 1 , n + 1 ) :
        for j in range ( min ( i , r ) , 0 , - 1 ) :
            C [ j ] = ( C [ j ] + C [ j - 1 ] ) % p
    return C [ r ]

if __name__ == '__main__':
    param = [
    (82,5,94,),
    (45,24,95,),
    (44,68,61,),
    (88,24,43,),
    (90,75,57,),
    (98,55,43,),
    (80,54,88,),
    (60,75,65,),
    (52,73,86,),
    (71,26,45,)
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
