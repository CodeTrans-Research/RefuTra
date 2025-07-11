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
import random
random.seed(1)
def f_gold ( arr , n ) :
    for i in range ( n - 1 , 0 , - 1 ) :
        j = random.randint ( 0 , i + 1 )
        arr [ i ] , arr [ j ] = arr [ j ] , arr [ i ]
    return arr


import random
def f_filled(arr, n):
    for i in range(n-1, 0, -1):
        j = random.randint(0, i)
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
    return arr

if __name__ == '__main__':
    param = [
    ([4, 4, 10, 10, 10, 12, 14, 16, 20, 21, 21, 22, 23, 25, 26, 28, 29, 29, 31, 32, 36, 38, 39, 40, 42, 43, 44, 46, 49, 56, 58, 61, 64, 67, 67, 73, 76, 80, 81, 82, 89, 89, 90, 92, 96, 97],38,),
    ([30, 78, -42, 0, 98, -58],3,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],32,),
    ([78, 5, 87, 36, 49, 89, 35, 84, 76, 91, 7, 64, 56, 80, 92, 10, 32, 7, 77, 97, 2, 60, 27, 65, 72, 39, 97],16,),
    ([-98, -98, -96, -94, -86, -86, -84, -84, -78, -76, -72, -52, -48, -46, -46, -40, -38, -32, -24, -24, 2, 4, 18, 18, 18, 24, 24, 24, 26, 40, 40, 42, 48, 50, 54, 56, 58, 62, 80, 88, 92],23,),
    ([1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1],21,),
    ([2, 15, 20, 37, 42, 50, 61, 99],7,),
    ([-14, 86, -46, 24, -4, 18, 88, -64, 72, 68, 22, -90, -78, -20, -70, -30, 12, 92, 68, -80, 88, 98, 6, 8, -34, 96, -68, -76, -68, 84, -78, 92, -32, -82, 14, -60],22,),
    ([0, 1],1,),
    ([23, 40, 62, 21, 87, 54, 76, 72, 76, 60, 89, 74, 13, 75, 91, 53, 96, 94, 12, 36, 60, 62, 55, 82, 27, 80, 97, 42, 25, 98, 9, 8, 45, 47, 55, 67, 91, 25],32,)
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

