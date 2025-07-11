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
def f_gold ( arr , n , x , k ) :
    i = 0
    while ( i < n ) :
        if ( arr [ i ] == x ) :
            return i
        i = i + max ( 1 , int ( abs ( arr [ i ] - x ) / k ) )
    print ( "number is not present!" )
    return - 1


def f_filled ( arr , n , x , k ) :
    i = 0
    while i < n :
        if arr [ i ] == x :
            return i
        i = i + max ( 1 , abs ( arr [ i ] - x ) // k )
    print ( "number is " + "not present!" )
    return - 1

if __name__ == '__main__':
    param = [
    ([1, 5, 9, 11, 14, 18, 19, 21, 26, 32, 38, 38, 43, 47, 49, 52, 55, 61, 65, 67, 69, 73, 74, 79, 84, 90, 91, 91, 92, 93, 94, 99],22,19,26,),
    ([12, -86, -66, -50, -48, 78, -92, -56, -2, 66, 64],5,10,5,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],35,37,43,),
    ([10, 87, 39, 87, 45, 33, 5, 37, 70, 69, 88, 78, 90, 3],9,8,10,),
    ([-78, -70, -68, -60, -52, -34, -24, -4, 12, 18, 58, 58, 64, 76, 84, 94],14,9,13,),
    ([0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0],26,36,32,),
    ([5, 5, 7, 11, 11, 15, 22, 23, 28, 38, 41, 53, 54, 57, 59, 68, 71, 89],16,17,16,),
    ([-4, 0, 60, -14, -48, 54, -96, -68, -40, 64, -50, -74, -20, -22, 48, -48, 42, 62, 66, 84, 54, -52, -52, 6, 46, -90, -18, 90],18,14,23,),
    ([0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],9,8,9,),
    ([30, 91, 34, 44, 3, 76, 43, 75, 49, 33, 74, 72, 68, 79, 26, 62, 23, 5, 32, 75, 82, 25, 7, 19, 32, 87, 87, 94, 34, 62, 3, 32, 59],32,30,24,)
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
