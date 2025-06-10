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
def f_gold ( n , m ) :
    count = [ ]
    for i in range ( n + 2 ) :
        count.append ( 0 )
    count [ 0 ] = 0
    for i in range ( 1 , n + 1 ) :
        if ( i > m ) :
            count [ i ] = count [ i - 1 ] + count [ i - m ]
        elif ( i < m ) :
            count [ i ] = 1
        else :
            count [ i ] = 2
    return count [ n ]


def f_filled ( n , m ) :
    count = [ 0 ] * ( n + 1 )
    count [ 0 ] = 0
    i = 0
    for i in range ( 1 , n + 1 ) :
        if i > m :
            count [ i ] = count [ i - 1 ] + count [ i - m ]
        elif i < m :
            count [ i ] = 1
        else :
            count [ i ] = 2
    return count [ n ]

if __name__ == '__main__':
    param = [
    (93,54,),
    (17,4,),
    (38,39,),
    (33,64,),
    (78,35,),
    (40,61,),
    (95,6,),
    (12,8,),
    (69,60,),
    (78,21,)
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
