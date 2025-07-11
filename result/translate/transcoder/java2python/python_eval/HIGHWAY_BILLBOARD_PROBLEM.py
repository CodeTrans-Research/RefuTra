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
def f_gold ( m , x , revenue , n , t ) :
    maxRev = [ 0 ] * ( m + 1 )
    nxtbb = 0 ;
    for i in range ( 1 , m + 1 ) :
        if ( nxtbb < n ) :
            if ( x [ nxtbb ] != i ) :
                maxRev [ i ] = maxRev [ i - 1 ]
            else :
                if ( i <= t ) :
                    maxRev [ i ] = max ( maxRev [ i - 1 ] , revenue [ nxtbb ] )
                else :
                    maxRev [ i ] = max ( maxRev [ i - t - 1 ] + revenue [ nxtbb ] , maxRev [ i - 1 ] ) ;
                nxtbb += 1
        else :
            maxRev [ i ] = maxRev [ i - 1 ]
    return maxRev [ m ]


def f_filled ( m , x , revenue , n , t ) :
    max_rev = [ 0 ] * m + [ 0 ] * m
    nxtbb = 0
    for i in range ( m + 1 ) :
        if nxtbb < n :
            if x [ nxtbb ] != i :
                max_rev [ i ] = max_rev [ i - 1 ]
            else :
                if i <= t :
                    max_rev [ i ] = max ( max_rev [ i - 1 ] , revenue [ nxtbb ] )
                else :
                    max_rev [ i ] = max ( max_rev [ i - t - 1 ] + revenue [ nxtbb ] , max_rev [ i - 1 ] )
                nxtbb += 1
        else :
            max_rev [ i ] = max_rev [ i - 1 ]
    return max_rev [ m ]

if __name__ == '__main__':
    param = [
    (16,[6, 15, 15, 18, 23, 29, 32, 36, 37, 39, 40, 41, 44, 49, 51, 52, 53, 57, 66, 68, 82, 89, 96],[1, 2, 5, 5, 24, 26, 31, 32, 33, 41, 57, 59, 71, 75, 79, 87, 87, 88, 92, 94, 96, 96, 99],12,12,),
    (39,[76, 60, 88, 46, -20, -78, -22, 54, -18, 92, -42, -66, -90, -72, -48, 22, -72, -42, -46, 94, 82, -78, 14, 86, 10, -64, -78, 66, 78, -36, 50, -20, -40, -12, 10, -46, 56, -18, 4, -76, -64, 74, 22, 34, 4, -2],[28, 8, -60, 84, 68, -54, -56, 0, -68, -84, -6, 92, -80, -24, 86, -6, -44, 82, 74, 90, -46, 40, 62, 50, -42, 38, 78, 94, 46, -14, -48, 66, 70, 52, 10, -88, 54, -10, 98, 34, 16, -2, -62, -56, -40, 86],25,27,),
    (5,[0, 0, 0, 1, 1, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0, 0, 1, 1, 1],9,6,),
    (10,[21, 69, 30, 10, 71, 72, 71, 78, 30, 9, 72, 10, 7, 87, 30, 46, 56, 74, 73, 60, 86],[72, 45, 7, 30, 76, 35, 75, 72, 4, 7, 55, 56, 7, 52, 48, 27, 11, 76, 66, 48, 33],18,20,),
    (14,[-76, -76, -66, -64, -62, -60, -52, -48, -42, -28, -14, -6, -6, 16, 20, 20, 38, 46, 58, 60, 70, 72, 86, 98],[-90, -82, -78, -76, -74, -52, -48, -44, -44, -40, -38, -14, -6, 10, 20, 38, 38, 40, 44, 48, 52, 54, 76, 78],15,17,),
    (32,[1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],[0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],28,36,),
    (2,[16, 38, 72, 82],[15, 34, 56, 74],2,3,),
    (22,[28, -76, 42, -2, 30, -10, 52, 66, 26, 96, 96, -72, 26, -86, -30, -78, 32, -32, 58, 12, -72, 8, 34, -68, -28, -66],[68, -38, 34, 20, 40, 78, 52, 80, 58, -12, -18, 10, 40, 34, 20, -32, -8, -46, 8, 62, 94, -30, -94, 26, -40, 64],13,16,),
    (15,[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],25,15,),
    (8,[95, 12, 65, 97, 92, 49, 94, 32, 37, 97, 9, 35],[25, 32, 14, 49, 90, 37, 92, 1, 8, 75, 50, 9],9,8,)
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
