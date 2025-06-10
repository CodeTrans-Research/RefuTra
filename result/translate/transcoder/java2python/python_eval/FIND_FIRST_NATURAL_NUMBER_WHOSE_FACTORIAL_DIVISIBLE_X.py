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
def f_gold ( x ) :
    i = 1 ;
    fact = 1 ;
    for i in range ( 1 , x ) :
        fact = fact * i
        if ( fact % x == 0 ) :
            break
    return i


def f_filled ( x ) :
    i = 1
    fact = 1
    for i in range ( 1 , x ) :
        fact = fact * i
        if fact % x == 0 :
            break
    return i

if __name__ == '__main__':
    param = [
    (67,),
    (47,),
    (57,),
    (89,),
    (67,),
    (40,),
    (16,),
    (83,),
    (93,),
    (43,)
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
