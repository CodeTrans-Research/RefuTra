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
def f_gold ( arr , N , k ) :
    maxSum = 0 ;
    arr.sort ( ) ;
    i = N - 1 ;
    while ( i > 0 ) :
        if ( arr [ i ] - arr [ i - 1 ] < k ) :
            maxSum += arr [ i ] ;
            maxSum += arr [ i - 1 ] ;
            i -= 1 ;
        i -= 1 ;
    return maxSum ;


def f_filled(arr, N, k):
        arr.sort()
        maxSum = 0
        for i in range(N - 1):
            if (arr[i]-arr[i-1]<k):
                maxSum += arr[i + 1] + arr[i]
                i -= 1
        return maxSum

if __name__ == '__main__':
    param = [
    ([2, 10, 11, 11, 12, 14, 15, 17, 27, 27, 28, 36, 36, 44, 47, 47, 54, 55, 62, 64, 68, 69, 70, 70, 75, 76, 78, 85, 85, 91, 95, 97],32,18,),
    ([-36, 78, 10, 30, -12, -70, -98, -14, -44, -66, -40, -8, 78, 2, -70, 40, 92, 58, 30, 10, -84, -62, -86, -50, 82, 36, -92, -30, -2, -34, 88, 2, -4, -72],34,25,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],48,26,),
    ([77, 78, 58],3,1,),
    ([-88, -88, -88, -82, -58, -54, -48, -46, -46, -44, -20, -2, 10, 28, 28, 28, 42, 42, 44, 50, 50, 54, 56, 58, 62, 68, 70, 72, 74, 76, 78, 88, 90, 92],34,24,),
    ([0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],43,40,),
    ([5, 7, 10, 11, 15, 17, 20, 20, 29, 29, 32, 37, 38, 39, 40, 41, 45, 51, 60, 64, 64, 68, 68, 70, 71, 71, 71, 75, 76, 82, 84, 87, 88, 88, 95, 98],36,21,),
    ([-46, -32, 76, -28, 44, -14, 94, -4, 60, -88, -52, 32, -66, 28, 94, 76, 86, -4, 74, 52, 64, -36, -98, -40, 70, 18, -22, -20, -16, -74, 12, 60, 94, 98, -28, -24, 4, -34, -60, 56],40,23,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],45,41,),
    ([79, 13, 25, 22, 61, 1, 2, 73, 66, 94, 47, 9, 1, 99, 25, 39, 95, 46, 95, 20, 63, 15, 14, 36, 9, 91, 14],27,23,)
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

