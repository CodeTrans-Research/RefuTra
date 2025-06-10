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
def f_gold ( n ) :
    a = [ 0 for i in range ( n ) ]
    b = [ 0 for i in range ( n ) ]
    a [ 0 ] = b [ 0 ] = 1
    for i in range ( 1 , n ) :
        a [ i ] = a [ i - 1 ] + b [ i - 1 ]
        b [ i ] = a [ i - 1 ]
    return a [ n - 1 ] + b [ n - 1 ]


def f_filled ( n ) :
    a = np.zeros ( ( n , n ) )
    b = np.zeros ( ( n , n ) )
    a [ 0 ] = b [ 0 ] = 1
    for i in range ( 1 , n ) :
        a [ i ] = a [ i - 1 ] + b [ i - 1 ]
        b [ i ] = a [ i - 1 ]
    return a [ n - 1 ] + b [ n - 1 ]

if __name__ == '__main__':
    param = [
    (86,),
    (75,),
    (14,),
    (5,),
    (41,),
    (35,),
    (30,),
    (89,),
    (84,),
    (53,)
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
