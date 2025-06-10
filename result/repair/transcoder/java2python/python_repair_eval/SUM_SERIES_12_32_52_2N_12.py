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
    sum = 0
    for i in range ( 1 , n + 1 ) :
        sum = sum + ( 2 * i - 1 ) * ( 2 * i - 1 )
    return sum


def f_filled ( n ) :
    sum = 0
    for i in range ( 1 , n + 1 ) :
        sum =  sum+(2*i-1)*(2*i-1)
    return sum

if __name__ == '__main__':
    param = [
    (14,),
    (61,),
    (37,),
    (86,),
    (47,),
    (98,),
    (70,),
    (24,),
    (76,),
    (24,)
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
