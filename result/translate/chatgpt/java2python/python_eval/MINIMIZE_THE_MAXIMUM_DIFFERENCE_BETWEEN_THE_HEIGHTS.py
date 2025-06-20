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
def f_gold ( arr , n , k ) :
    if ( n == 1 ) :
        return 0
    arr.sort ( )
    ans = arr [ n - 1 ] - arr [ 0 ]
    small = arr [ 0 ] + k
    big = arr [ n - 1 ] - k
    if ( small > big ) :
        small , big = big , small
    for i in range ( 1 , n - 1 ) :
        subtract = arr [ i ] - k
        add = arr [ i ] + k
        if ( subtract >= small or add <= big ) :
            continue
        if ( big - subtract <= add - small ) :
            small = subtract
        else :
            big = add
    return min ( ans , big - small )


def f_filled(arr, n, k):
    if n == 1:
        return 0

    arr.sort()
    ans = arr[n - 1] - arr[0]
    small = arr[0] + k
    big = arr[n - 1] - k
    temp = 0

    if small > big:
        temp = small
        small = big
        big = temp

    for i in range(1, n - 1):
        subtract = arr[i] - k
        add = arr[i] + k
        if subtract >= small or add <= big:
            continue
        if big - subtract <= add - small:
            small = subtract
        else:
            big = add

    return min(ans, big - small)

if __name__ == '__main__':
    param = [
        ([31, 33, 40, 43, 44, 51, 52, 56, 60, 64, 66, 79, 91, 93, 99], 15, 13,),
        ([-16, 34, 54, -86, -62], 5, 4,),
        ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 31, 22,),
        ([27, 84, 57, 45, 70, 41, 67, 3, 5, 67, 16, 74, 99, 90, 48, 90, 7, 86, 59, 88, 45, 11, 21, 91, 17, 67, 59, 60,
          36, 9, 5, 55, 68, 58, 91, 51, 44, 92, 77, 38], 40, 28,),
        ([-88, -84, -78, -72, -66, -66, -58, -56, -56, -56, -54, -50, -50, -38, -24, -18, -12, -10, -8, -4, 0, 6, 8, 10,
          14, 40, 44, 50, 58, 64, 64, 68], 32, 28,),
        ([1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0], 11, 8,),
        ([6, 11, 13, 14, 22, 25, 26, 28, 30, 31, 37, 37, 55, 57, 61, 62, 64, 67, 69, 70, 71, 73, 73, 75, 80, 81, 82, 88,
          90, 98], 30, 26,),
        (
        [-86, 4, -90, 66, -10, -36, -18, 82, 20, 6, -78, 98, -64, 52, -22, 20, 44, -70, -32, 88, -80, 24, -38, -62, 92],
        25, 18,),
        ([0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 25, 19,),
        ([2], 1, 0,)
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

