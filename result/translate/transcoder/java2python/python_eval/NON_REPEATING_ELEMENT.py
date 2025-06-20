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
def f_gold ( arr , n ) :
    for i in range ( n ) :
        j = 0
        while ( j < n ) :
            if ( i != j and arr [ i ] == arr [ j ] ) :
                break
            j += 1
        if ( j == n ) :
            return arr [ i ]
    return - 1


def f_filled ( arr , n ) :
    for i in range ( n ) :
        j = 0
        for j in range ( n ) :
            if i != j and arr [ i ] == arr [ j ] :
                break
        if j == n :
            return arr [ i ]
    return - 1

if __name__ == '__main__':
    param = [
    ([1, 2, 3, 4, 6, 6, 7, 9, 10, 13, 16, 23, 30, 32, 36, 42, 42, 43, 44, 47, 48, 48, 49, 52, 52, 53, 55, 56, 58, 59, 60, 60, 63, 67, 68, 68, 74, 75, 76, 80, 81, 81, 83, 83, 86, 87, 91, 92, 97],47,),
    ([-96, -46, -86, 56, -72, 50, 18, 8, 50],8,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],14,),
    ([19, 10, 49, 40, 34, 21, 63, 51],5,),
    ([-96, -96, -90, -88, -88, -84, -80, -76, -68, -64, -64, -52, -52, -52, -52, -50, -50, -48, -48, -40, -32, -26, -24, -22, -20, -14, -12, 0, 6, 8, 10, 20, 24, 28, 34, 36, 54, 60, 60, 60, 68, 74, 74, 74, 84, 88, 94],27,),
    ([1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0],19,),
    ([1, 2, 3, 10, 15, 21, 28, 36, 41, 44, 45, 47, 72, 77, 77, 79, 85],15,),
    ([42, -84, 42, 36, -10, 24, -62, 60],7,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],35,),
    ([2, 21, 42, 92, 65, 62, 75, 43, 81, 17, 92, 86, 37, 63, 27, 97, 24, 61, 85, 49, 84, 7, 14, 19, 60, 55, 68, 79, 8, 12, 75, 12, 92, 79, 42],27,)
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
