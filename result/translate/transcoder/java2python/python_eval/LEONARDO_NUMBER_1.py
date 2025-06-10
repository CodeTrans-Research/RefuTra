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
    dp = [ ] ;
    dp.append ( 1 ) ;
    dp.append ( 1 ) ;
    for i in range ( 2 , n + 1 ) :
        dp.append ( dp [ i - 1 ] + dp [ i - 2 ] + 1 ) ;
    return dp [ n ] ;


def f_filled ( n ) :
    dp = [ 0 ] * ( n + 1 )
    dp [ 0 ] = dp [ 1 ] = 1
    for i in range ( 2 , n + 1 ) :
        dp [ i ] = dp [ i - 1 ] + dp [ i - 2 ] + 1
    return dp [ n ]

if __name__ == '__main__':
    param = [
    (75,),
    (76,),
    (55,),
    (14,),
    (43,),
    (10,),
    (16,),
    (30,),
    (44,),
    (65,)
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
