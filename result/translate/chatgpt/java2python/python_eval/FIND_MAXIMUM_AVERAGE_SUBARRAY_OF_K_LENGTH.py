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
    if k > n :
        return - 1
    csum = [ 0 ] * n
    csum [ 0 ] = arr [ 0 ]
    for i in range ( 1 , n ) :
        csum [ i ] = csum [ i - 1 ] + arr [ i ] ;
    max_sum = csum [ k - 1 ]
    max_end = k - 1
    for i in range ( k , n ) :
        curr_sum = csum [ i ] - csum [ i - k ]
        if curr_sum > max_sum :
            max_sum = curr_sum
            max_end = i
    return max_end - k + 1


def f_filled(arr, n, k):
    if k > n:
        return -1
    csum = [0] * n
    csum[0] = arr[0]
    for i in range(1, n):
        csum[i] = csum[i - 1] + arr[i]
    max_sum = csum[k - 1]
    max_end = k - 1
    for i in range(k, n):
        curr_sum = csum[i] - csum[i - k]
        if curr_sum > max_sum:
            max_sum = curr_sum
            max_end = i
    return max_end - k + 1

if __name__ == '__main__':
    param = [
    ([2, 4, 6, 19, 21, 23, 32, 34, 47, 51, 56, 57, 57, 65, 68, 68, 69, 70, 71, 73, 74, 74, 77, 77, 79, 82, 82, 86, 87, 87, 88, 89, 90, 91, 92],29,20,),
    ([24, 62, -32, -28, 42, -46, -96, -70, -68, 60, 44, 34, -30, 96, -26, 92, 62, 42, -46, -38, 44, 54, -94, 52, 66, 68, -96, -58, 84, -2, 66, 30, 42],23,31,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],32,31,),
    ([94, 6, 48, 34, 31],4,3,),
    ([-98, -88, -82, -80, -76, -70, -70, -60, -60, -52, -50, -46, -44, -44, -44, -20, -18, -12, -12, -12, -10, -8, -6, -4, 4, 4, 18, 28, 32, 34, 42, 42, 44, 46, 48, 54, 60, 70, 70, 72, 78, 78, 78, 78, 84, 86, 90, 96, 98],45,30,),
    ([0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0],15,8,),
    ([1, 5, 13, 17, 26, 26, 32, 35, 38, 38, 39, 45, 52, 58, 60, 61, 62, 63, 82, 83, 85, 89, 89, 91],13,22,),
    ([-68, -52, 4, -90, 90, 88, 38, -18, 86, 4, 14, -32, -14, -44, -88, -50, -12, -26, -68, -20, -30, 22, 0, 14, -40, 58, -6, 28, -44, 8, 28, 96, -46, -12],32,22,),
    ([0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],13,11,),
    ([17, 33, 36, 34, 32, 10, 37, 48, 47, 32, 21, 18, 75, 8, 18, 52, 21, 73, 25, 25, 80, 32, 10, 24, 1, 89, 7, 42, 86, 85, 73, 12, 20, 20, 1, 74, 77, 4, 24, 74, 8],20,28,)
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
