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
    mpis = [ 0 ] * ( n )
    for i in range ( n ) :
        mpis [ i ] = arr [ i ]
    for i in range ( 1 , n ) :
        for j in range ( i ) :
            if ( arr [ i ] > arr [ j ] and mpis [ i ] < ( mpis [ j ] * arr [ i ] ) ) :
                mpis [ i ] = mpis [ j ] * arr [ i ]
    return max ( mpis )


def f_filled ( arr , n ) :
    mpis = [ ]
    max = int ( arr [ i ] )
    for i in range ( n ) :
        mpis.append ( arr [ i ] )
    for i in range ( 1 , n ) :
        for j in range ( i ) :
            if arr [ i ] > arr [ j ] and mpis [ i ] < ( mpis [ j ] * arr [ i ] ) :
                mpis [ i ] = mpis [ j ] * arr [ i ]
    for k in mpis :
        if mpis [ k ] > max :
            max = mpis [ k ]
    return max

if __name__ == '__main__':
    param = [
    ([1, 1, 4, 7, 7, 9, 12, 20, 45, 53, 58, 63, 65, 65, 86, 98, 98],12,),
    ([46, -58, 70, 60, 74, 42, 6, -26, 78, 32, 14, -56, -48, 86, -2, 94, -44, -62, -50, -8, -4, -36, -62, -98, -98, -78, 56, 92, 88],27,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],14,),
    ([13, 71, 93, 68, 43, 75, 44, 15, 1, 91, 7, 9, 65, 85, 46, 87, 37, 74, 19, 30, 87, 27, 82, 92, 12, 36, 6, 27, 76, 80, 30, 83, 67, 83, 65, 28, 81, 59, 63, 11, 70],20,),
    ([-96, -94, -92, -88, -84, -80, -74, -70, -62, -56, -48, -46, -40, -34, -32, -26, -22, -22, -12, -10, -8, -6, -2, 0, 2, 4, 6, 18, 18, 30, 34, 34, 38, 38, 40, 48, 54, 56, 60, 84, 88, 88, 90, 94, 96],30,),
    ([1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],22,),
    ([1, 1, 5, 5, 6, 7, 18, 35, 39, 51, 64, 73, 87, 90, 91, 92],11,),
    ([-54, 8, -92, -28, 72, 54, -74, 36, -10, 54, -30, -16, -72, -32, -92, 38, -76, -76, -50, -92, 48],19,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],26,),
    ([47, 57, 72, 40, 53, 46, 62, 51, 42, 89, 9, 91, 58, 67, 20, 91, 63, 50, 32, 6, 63, 49, 3, 89, 87, 54, 65, 72, 72, 62, 31, 6, 48, 87, 17, 95, 59, 57],30,)
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
