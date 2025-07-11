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
def f_gold ( arr1 , arr2 , m , n , x ) :
    count = 0
    for i in range ( m ) :
        for j in range ( n ) :
            if arr1 [ i ] + arr2 [ j ] == x :
                count = count + 1
    return count


def f_filled ( arr1 , arr2 , m , n , x ) :
    count = 0
    for i in range ( m ) :
        for j in range ( n ) :
            if ( arr1 [ i ] + arr2 [ j ] ) == x :
                count += 1
    return count

if __name__ == '__main__':
    param = [
    ([11, 13, 16, 23, 26, 28, 31, 34, 37, 39, 44, 48, 56, 59, 79, 91, 96, 98],[1, 1, 9, 14, 17, 23, 26, 31, 33, 36, 53, 60, 71, 75, 76, 84, 87, 88],9,15,11,),
    ([50, 14, -98, 14, 90, 36, 66, 44, 10, -98, -24, -36, -32, -50],[34, -6, -66, 0, -6, 82, 60, -98, -8, 60, -2, 4, 22, 76],11,12,8,),
    ([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],14,9,12,),
    ([88, 14, 29, 87, 86, 58],[91, 95, 64, 4, 63, 35],3,5,5,),
    ([-98, -92, -88, -86, -82, -76, -72, -66, -56, -48, -34, -28, -28, -26, -20, -18, -18, -16, -16, -12, -4, 0, 6, 12, 16, 20, 22, 30, 34, 34, 36, 56, 58, 62, 64, 80, 82, 94],[-94, -90, -88, -84, -82, -78, -76, -72, -70, -58, -58, -46, -42, -40, -40, -32, -22, -20, -18, -12, -8, -6, 6, 6, 18, 20, 34, 46, 60, 62, 66, 72, 72, 76, 76, 78, 92, 98],34,32,23,),
    ([1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0],[1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0],39,26,34,),
    ([70, 70, 74],[15, 55, 84],1,1,1,),
    ([-20, -12, -50, 76, 24, 64, -22, -4, -68],[18, 98, -88, 86, 72, -44, 82, 94, 58],5,4,7,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],27,26,37,),
    ([68, 75, 51, 45, 73, 95, 48, 53, 70, 41, 65, 47, 46, 43, 79, 29, 50],[4, 6, 76, 65, 16, 13, 85, 43, 31, 14, 81, 90, 24, 87, 40, 25, 88],10,10,9,)
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
