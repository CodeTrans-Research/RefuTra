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
    nCr = 1
    res = 1
    for r in range ( 1 , n + 1 ) :
        nCr = ( nCr * ( n + 1 - r ) ) // r 
        res += nCr * nCr 
    return res 


def f_filled ( n ) :
    nCr , res = 1 , 1
    for r in range ( 1 , n + 1 ) :
        nCr =  (nCr*(n+1-r))//r
        res += nCr ** 2
    return res

if __name__ == '__main__':
    param = [
    (52,),
    (75,),
    (25,),
    (80,),
    (18,),
    (17,),
    (33,),
    (8,),
    (99,),
    (8,)
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
