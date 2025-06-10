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
    dp = [ 0 for i in range ( n + 1 ) ]
    for i in range ( n + 1 ) :
        if ( i <= 2 ) :
            dp [ i ] = i
        else :
            dp [ i ] = dp [ i - 1 ] + ( i - 1 ) * dp [ i - 2 ]
    return dp [ n ]


def f_filled ( n ) :
    dp = [ ]
    for i in range ( 0 , n + 1 ) :
        if i <= 2 :
            dp.append ( i )
        else :
            dp.append ( dp [ i - 1 ] + ( i - 1 ) * dp [ i - 2 ] )
    return dp [ n ]

if __name__ == '__main__':
    param = [
    (99,),
    (62,),
    (87,),
    (87,),
    (61,),
    (88,),
    (73,),
    (62,),
    (98,),
    (57,)
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
