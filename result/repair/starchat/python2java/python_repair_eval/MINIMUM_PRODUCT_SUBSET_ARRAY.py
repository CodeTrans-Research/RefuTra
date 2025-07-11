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
def f_gold ( a , n ) :
    if ( n == 1 ) :
        return a [ 0 ]
    max_neg = float ( '-inf' )
    min_pos = float ( 'inf' )
    count_neg = 0
    count_zero = 0
    prod = 1
    for i in range ( 0 , n ) :
        if ( a [ i ] == 0 ) :
            count_zero = count_zero + 1
            continue
        if ( a [ i ] < 0 ) :
            count_neg = count_neg + 1
            max_neg = max ( max_neg , a [ i ] )
        if ( a [ i ] > 0 ) :
            min_pos = min ( min_pos , a [ i ] )
        prod = prod * a [ i ]
    if ( count_zero == n or ( count_neg == 0 and count_zero > 0 ) ) :
        return 0 ;
    if ( count_neg == 0 ) :
        return min_pos
    if ( ( count_neg & 1 ) == 0 and count_neg != 0 ) :
        prod = int ( prod / max_neg )
    return prod ;


def f_filled(a, n):
        if n == 1:
            return a[0]
        negmax = float("inf")
        posmin = float("-inf")
        count_neg = 0
        count_zero = 0
        product = 1
        for i in range(n):
            if a[i] == 0:
                count_zero += 1
            elif a[i] < 0:
                count_neg += 1
                negmax = max(negmax, a[i])
            elif a[i] > 0 and a[i] < posmin:
                posmin = a[i]
            product *= a[i]
        if count_zero == n or (count_neg == 0 and count_zero > 0):
            return 0
        if count_neg == 0:
            return posmin
        if count_neg % 2 == 0 and count_neg!= 0:
            product //= negmax
        return product

if __name__ == '__main__':
    param = [
    ([3, 6, 7, 8, 8, 9, 12, 12, 12, 13, 15, 15, 15, 16, 18, 18, 18, 19, 20, 21, 22, 22, 23, 28, 29, 30, 30, 33, 33, 35, 35, 36, 40, 43, 58, 63, 73, 78, 82, 83, 84, 87, 89, 89, 92, 94],23,),
    ([18, -6, -8, 98, 66, -86, 24, 6, 58, 74, 82],10,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],25,),
    ([97, 79, 93, 41, 76, 34, 94, 57, 63, 98, 52, 62, 96, 7, 63, 44, 55, 43, 36, 66, 35, 14, 24, 40, 26, 16, 67, 19, 31, 86, 64, 93, 85, 86, 66, 24, 73, 86, 45, 99, 25, 98, 38, 57],30,),
    ([],0,),
    ([1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0],36,),
    ([1, 3, 5, 15, 18, 19, 21, 23, 29, 29, 33, 33, 34, 37, 39, 43, 43, 68, 73, 74, 75, 84, 87, 88, 89, 90, 93],18,),
    ([74, 70, -36, 16, 10, 60, -82, 96, -30, 58, 56, -54, -14, 94, 10, -82, -80, -40, -72, -68, 8, 38, -50, -76, 34, 2, -66, -30, 26],15,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],20,),
    ([74, 74, 8, 74, 85, 41, 31, 3, 84, 46, 73, 39, 64, 72, 28, 83, 98, 27, 64, 7, 95, 37, 10, 38, 77, 32, 69, 72, 62, 96, 5, 81, 34, 96, 80, 25, 38],33,)
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
