import sys
import math
import heapq
from queue import Queue# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
import math

def f_gold ( arr , n ) :
    min_prefix_sum = 0
    res = - math.inf
    prefix_sum = [ ]
    prefix_sum.append ( arr [ 0 ] )
    for i in range ( 1 , n ) :
        prefix_sum.append ( prefix_sum [ i - 1 ] + arr [ i ] )
    for i in range ( n ) :
        res = max ( res , prefix_sum [ i ] - min_prefix_sum )
        min_prefix_sum = min ( min_prefix_sum , prefix_sum [ i ] )
    return res


def f_filled(arr, n):
        min_prefix_sum = 0
        res = sys.maxsize
        prefix_sum = [0] * n
        prefix_sum[0] = arr[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i-1] + arr[i]
        for i in range(n):
            res = max(res, prefix_sum[i] - min_prefix_sum)
            min_prefix_sum = min(min_prefix_sum, prefix_sum[i])
        return res

if __name__ == '__main__':
    param = [
    ([8, 9, 11, 17, 18, 19, 23, 24, 27, 30, 31, 31, 35, 44, 46, 47, 49, 51, 55, 58, 59, 61, 65, 67, 71, 71, 71, 71, 78, 78, 82, 91, 98],20,),
    ([-82, -28, -66, -52, -36, 36, -88, 52, -62, 46, 42, 26, -60, 18, -52, 38, 94, -68, 44, -94, 14, 36, -70],15,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],19,),
    ([28, 36, 42, 42, 5, 52, 74, 86, 55, 82, 59, 81, 4, 90, 24, 34, 20, 99, 86, 25, 52, 48, 62, 5, 67, 83, 60, 72, 80, 73, 38, 55, 8, 70, 95],19,),
    ([-92, -52, -24, 36, 56],3,),
    ([0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0],13,),
    ([1, 1, 4, 4, 7, 7, 17, 18, 20, 26, 26, 32, 37, 38, 42, 44, 44, 46, 50, 53, 57, 58, 58, 60, 61, 61, 64, 74, 75, 77, 83, 83, 84, 84, 85, 87, 88, 90, 95, 96, 97, 98, 99, 99],25,),
    ([-86, 2, 26, 54, -16, 16, 48, 24, 50, -10, -32, -62, 48, -12, -66],13,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],14,),
    ([58, 14, 79, 11, 31, 28, 61, 86, 25, 27, 75, 78, 32, 55, 86, 48, 15, 51, 6, 78, 23, 82, 16, 62, 35, 51, 91, 16, 79, 38, 97, 30, 23, 58, 95, 57, 82, 35, 57, 43, 22, 41, 58, 69, 25, 65, 13, 79],39,)
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
