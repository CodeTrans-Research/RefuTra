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
def f_gold ( p , q ) :
    dp = [ 0 for i in range ( q ) ]
    dp[0] = 1
    for i in range ( p ) :
        for j in range ( 1 , q ) :
            dp [ j ] += dp [ j - 1 ]
    return dp [ q - 1 ]


def f_filled ( m , n ) :
    dp = np.zeros ( ( n , m ) )
    dp [ 0 ] = 1
    for i in range ( m ) :
        for j in range ( 1 , n ) :
            dp [ j ] += dp [ j - 1 ]
    return dp [ n - 1 ]

if __name__ == '__main__':
    param = [
    (73,75,),
    (70,5,),
    (53,62,),
    (80,70,),
    (9,59,),
    (38,48,),
    (41,49,),
    (80,72,),
    (42,52,),
    (54,1,)
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
