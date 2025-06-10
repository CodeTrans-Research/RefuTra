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
    res = 0
    x = 0
    while ( x * x < n ) :
        y = 0
        while ( x * x + y * y < n ) :
            res = res + 1
            y = y + 1
        x = x + 1
    return res


def f_filled ( n ) :
    res = 0
    for x in range ( 0 , n * x ) :
        for y in range ( 0 , x * x + y * y ) :
            res += 1
    return res

if __name__ == '__main__':
    param = [
    (61,),
    (45,),
    (53,),
    (4,),
    (82,),
    (86,),
    (37,),
    (48,),
    (81,),
    (50,)
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
