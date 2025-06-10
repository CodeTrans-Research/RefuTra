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
    count = 0
    for i in range ( 0 , n + 1 ) :
        for j in range ( 0 , n + 1 ) :
            for k in range ( 0 , n + 1 ) :
                if ( i + j + k == n ) :
                    count = count + 1
    return count


def f_filled ( n ) :
    count = 0
    for i in range ( 0 , n ) :
        for j in range ( 0 , n ) :
            for k in range ( 0 , n ) :
                if i + j + k == n :
                    count += 1
    return count

if __name__ == '__main__':
    param = [
    (52,),
    (47,),
    (75,),
    (36,),
    (68,),
    (16,),
    (99,),
    (38,),
    (84,),
    (45,)
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
