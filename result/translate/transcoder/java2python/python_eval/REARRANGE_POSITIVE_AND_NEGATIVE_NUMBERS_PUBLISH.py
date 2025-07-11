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
    i = - 1
    for j in range ( n ) :
        if ( arr [ j ] < 0 ) :
            i += 1
            arr [ i ] , arr [ j ] = arr [ j ] , arr [ i ]
    pos , neg = i + 1 , 0
    while ( pos < n and neg < pos and arr [ neg ] < 0 ) :
        arr [ neg ] , arr [ pos ] = arr [ pos ] , arr [ neg ]
        pos += 1
        neg += 2


def f_filled ( arr , n ) :
    i , temp = - 1 , 0
    for j in range ( n ) :
        if arr [ j ] < 0 :
            i += 1
            temp = arr [ i ]
            arr [ i ] , arr [ j ] = arr [ j ] , temp
    pos , neg = i + 1 , 0
    while pos < n and neg < pos and arr [ neg ] < 0 :
        temp = arr [ neg ]
        arr [ neg ] , arr [ pos ] = arr [ pos ] , temp
        pos += 1
        neg += 2
    return arr , temp

if __name__ == '__main__':
    param = [
    ([5, 5, 6, 7, 8, 10, 13, 15, 15, 27, 27, 29, 29, 29, 29, 31, 33, 33, 36, 38, 38, 39, 42, 47, 47, 51, 51, 51, 52, 53, 55, 56, 57, 64, 66, 66, 67, 68, 70, 72, 74, 78, 86, 88, 94, 97, 97],26,),
    ([73, 30, 55, -5, 15, 64, -64, -74, -57, -73, -31, 48],8,),
    ([0, 0, 0, 1, 1, 1, 1, 1, 1, 1],6,),
    ([62, 82, 89, 97, 60, 43, 76, 68, 5, 37, 72, 92, 31],7,),
    ([-99, -89, -71, -60, -59, -54, -49, 1, 51],8,),
    ([1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1],21,),
    ([2, 7, 17, 22, 24, 25, 26, 28, 29, 33, 34, 38, 43, 49, 51, 52, 54, 59, 63, 70, 71, 75, 82, 88, 91, 91],14,),
    ([-51, 99, -19, -16, 5, 77, 48, 18, -14, -37, 89, 4, -51, -29, -99, 41, 79, 23, 84, -38, -68],10,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],44,),
    ([88, 87, 59],1,)
        ]
    filled_function_param = [
    ([5, 5, 6, 7, 8, 10, 13, 15, 15, 27, 27, 29, 29, 29, 29, 31, 33, 33, 36, 38, 38, 39, 42, 47, 47, 51, 51, 51, 52, 53, 55, 56, 57, 64, 66, 66, 67, 68, 70, 72, 74, 78, 86, 88, 94, 97, 97],26,),
    ([73, 30, 55, -5, 15, 64, -64, -74, -57, -73, -31, 48],8,),
    ([0, 0, 0, 1, 1, 1, 1, 1, 1, 1],6,),
    ([62, 82, 89, 97, 60, 43, 76, 68, 5, 37, 72, 92, 31],7,),
    ([-99, -89, -71, -60, -59, -54, -49, 1, 51],8,),
    ([1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1],21,),
    ([2, 7, 17, 22, 24, 25, 26, 28, 29, 33, 34, 38, 43, 49, 51, 52, 54, 59, 63, 70, 71, 75, 82, 88, 91, 91],14,),
    ([-51, 99, -19, -16, 5, 77, 48, 18, -14, -37, 89, 4, -51, -29, -99, 41, 79, 23, 84, -38, -68],10,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],44,),
    ([88, 87, 59],1,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        f_filled(*(filled_function_param[i]))
        f_gold(*parameters_set)
        if parameters_set == filled_function_param[i]:
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))
