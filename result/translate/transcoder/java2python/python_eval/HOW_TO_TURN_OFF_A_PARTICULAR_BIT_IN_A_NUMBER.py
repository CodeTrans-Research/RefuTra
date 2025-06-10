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
    if ( k <= 0 ) :
        return n
    return ( n & ~ ( 1 << ( k - 1 ) ) )


def f_filled ( n , k ) :
    if k <= 0 :
        return n
    return ( n & ~ ( 1 << ( k - 1 ) ) )

if __name__ == '__main__':
    param = [
    (49,15,),
    (59,69,),
    (76,20,),
    (27,76,),
    (61,60,),
    (67,27,),
    (63,71,),
    (85,25,),
    (90,64,),
    (24,55,)
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
