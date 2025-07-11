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
def f_gold ( arr , n , k ) :
    if ( k > n ) :
        return - 1
    sum = arr [ 0 ]
    for i in range ( 1 , k ) :
        sum += arr [ i ]
    max_sum = sum
    max_end = k - 1
    for i in range ( k , n ) :
        sum = sum + arr [ i ] - arr [ i - k ]
        if ( sum > max_sum ) :
            max_sum = sum
            max_end = i
    return max_end - k + 1


def f_filled ( arr , n , k ) :
    if k > n :
        return - 1
    sum = arr [ 0 ]
    for i in range ( k ) :
        sum += arr [ i ]
    max_sum , max_end = sum , k - 1
    for i in range ( k , n ) :
        sum = sum + arr [ i ] - arr [ i - k ]
        if sum > max_sum :
            max_sum = sum
            max_end = i
    return max_end - k + 1

if __name__ == '__main__':
    param = [
    ([2, 5, 11, 37, 41, 49, 49, 63, 98],8,7,),
    ([84, -72, 12, 0, 86, -32, -18, 48, 60, 42, 8, -6, -10, -6, -52, -84, -98, 76, -10, -14, -94, -48, 94, -10, -20, 40, -52, 0, 94, -68, 44, -34, -26, -6, -94, 34, -80, -62, -40, 56, 52, -20, 74, -46, -88, -26, 22],34,43,),
    ([0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],11,18,),
    ([94, 97, 74, 88, 14, 66, 65, 50, 76, 55, 70, 93, 53, 30, 2, 60, 65, 24, 80, 73, 84, 95, 49, 32, 55, 70, 17, 26, 96, 20, 36, 2, 89, 49, 83, 67, 42, 51, 71, 11, 61, 78, 17, 78, 94, 68],35,33,),
    ([-98, -90, -60, -38, 38, 42],3,5,),
    ([1, 0, 0, 1, 1, 1, 1],3,4,),
    ([4, 9, 17, 17, 19, 32, 35, 36, 37, 40, 44, 45, 47, 48, 48, 56, 56, 60, 61, 65, 66, 79, 83, 91, 93, 99],22,24,),
    ([78, 82, -92, -46, -16, -64, 28, 60, 64, 52, 54, -84, 70, 22, 24, 0, -14, 20, -90, 30, 0, 86, 12, 72, -64, -52, 86, 16, -42],25,27,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],25,20,),
    ([81, 77, 6, 3, 72, 24, 75, 47, 17, 29, 69, 15, 15, 50, 30, 83, 11, 7, 59, 7, 12, 82, 45, 76, 9, 48, 98, 49, 29, 66, 3, 53, 37, 13, 72, 58, 37, 87, 55],34,23,)
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
