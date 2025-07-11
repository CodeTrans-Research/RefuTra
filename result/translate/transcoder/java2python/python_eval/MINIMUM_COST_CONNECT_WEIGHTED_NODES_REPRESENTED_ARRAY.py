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
import sys

def f_gold ( a , n ) :
    mn = sys.maxsize
    sum = 0
    for i in range ( n ) :
        mn = min ( a [ i ] , mn )
        sum += a [ i ]
    return mn * ( sum - mn )


def f_filled ( a , n ) :
    mn = int ( a [ 0 ] )
    sum = 0
    for i in range ( n ) :
        mn = min ( a [ i ] , mn )
        sum += a [ i ]
    return mn * ( sum - mn )

if __name__ == '__main__':
    param = [
    ([3, 8, 14, 15, 17, 17, 19, 21, 22, 23, 29, 32, 36, 37, 43, 45, 46, 47, 47, 53, 57, 57, 70, 71, 72, 76, 81, 82, 90, 95, 96, 98, 99],32,),
    ([94, -18, 50, 94, -74, -50, -44, -92, -58, 14, -66, -78],10,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],24,),
    ([],0,),
    ([-96, -88, -88, -84, -82, -78, -78, -60, -58, -56, -54, -52, -48, -44, -28, -26, -14, -12, 6, 10, 10, 14, 14, 50, 52, 54, 60, 62, 62, 64, 66, 70, 72, 72, 78, 80, 84],31,),
    ([0, 1, 1, 0, 1, 1, 1, 1],6,),
    ([3, 10, 14, 14, 15, 16, 18, 20, 21, 30, 31, 33, 35, 39, 46, 48, 59, 59, 61, 77, 78, 79, 81, 83, 85, 92, 97, 97, 99],23,),
    ([4, -32, 68, -48, 54, 24, 78, 98, -70, 44, -82, -92, -16, -92, -70, 52, -58, -62, -58, 32, 14, -4, 80, -78, -26, -24, -8],18,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],35,),
    ([82, 74, 53, 91, 81, 88, 42, 62, 38, 43, 29, 60, 43, 44, 19, 28, 20, 1, 5, 94, 18, 77, 52, 38, 55, 1, 10, 29, 34, 91, 64, 80, 81, 39, 4, 47, 30, 62, 58, 66, 73, 52, 62, 9, 36, 49],38,)
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
