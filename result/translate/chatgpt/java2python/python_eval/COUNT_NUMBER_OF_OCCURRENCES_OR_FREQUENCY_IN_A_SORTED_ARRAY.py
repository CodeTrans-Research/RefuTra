import sys
import math
import heapq
from queue import Queue
# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( arr , n , x ) :
    res = 0
    for i in range ( n ) :
        if x == arr [ i ] :
            res += 1
    return res


def f_filled(arr, n, x):
    res = 0
    for i in range(n):
        if x == arr[i]:
            res += 1
    return res

if __name__ == '__main__':
    param = [
    ([16, 18, 24, 27, 34, 36, 41, 43, 43, 52, 59, 76, 86, 87, 90, 91, 94, 96, 98, 98],14,43,),
    ([64, 66, -36],1,64,),
    ([0, 0, 0],2,0,),
    ([9, 85, 34, 43, 70, 96, 44, 7, 27, 33, 34, 5, 91, 84, 76, 45, 20, 37, 15, 37, 20, 24, 13, 49, 74, 13, 50, 81, 81, 66, 23, 36, 91, 80, 61, 15, 96, 70, 90, 25, 16, 62, 75, 63, 6, 65, 38, 12],43,5,),
    ([-98, -98, -98, -34, -32, -26, -12, 0, 18, 52, 68, 72],11,-98,),
    ([1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1],11,1,),
    ([1, 3, 6, 6, 10, 12, 15, 16, 21, 22, 23, 29, 33, 37, 40, 40, 43, 52, 55, 59, 64, 65, 71, 72, 80, 83, 86, 86, 88, 88],29,40,),
    ([-14, -30, -38, -38, -8, 40, -34, 2, -84, 68, -42, 38, -14, 0, -64, 12, -2, -38, -8, -44, -88, -34, -80, -36, 82, 70, 96, -32, 16, -52, -12, -46, -28, -86, 30, -14, 50, -44, 22, 30, -4, 78, 52],39,26,),
    ([1, 1, 1, 1],2,3,),
    ([11, 50, 1, 93, 12, 7, 55, 35, 36, 62, 61, 71, 16],11,8,)
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
            if set([filledres,goldres]) == set([float("inf"),sys.maxsize]) or set([filledres,goldres]) <= set([float("-inf"),-sys.maxsize-1,-sys.maxsize]):
                n_success += 1
    print("#Results: %i, %i" % (n_success, len(param)))
