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
def f_gold ( arr , low , high , key ) :
    if ( high < low ) :
        return - 1
    mid = ( low + high ) / 2
    if ( key == arr [ int ( mid ) ] ) :
        return mid
    if ( key > arr [ int ( mid ) ] ) :
        return f_gold ( arr , ( mid + 1 ) , high , key )
    return ( f_gold ( arr , low , ( mid - 1 ) , key ) )


def f_filled ( arr , low , high , key ) :
    if high < low :
        return - 1
    mid = ( low + high ) // 2
    if key == arr [ mid ] :
        return mid
    if key > arr [ mid ] :
        return f_filled ( arr , ( mid + 1 ) , high , key )
    return f_filled ( arr , low , ( mid - 1 ) , key )

if __name__ == '__main__':
    param = [
    ([2, 10, 73, 91, 98],2,4,4,),
    ([30, 24, 24, -8, 64, 50, 46, -76, 26, 8, -92, -78, 40, -86, 96, 14, 60, 38, 6, -72, -6, -20, 26, -26, 0, 2],20,13,21,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],30,27,29,),
    ([30, 79, 3, 76, 18],3,2,2,),
    ([-96, -90, -88, -84, -78, -78, -70, -68, -66, -66, -64, -64, -58, -56, -52, -42, -40, -38, -36, -30, -30, -28, -14, -8, 0, 14, 16, 22, 24, 26, 36, 40, 40, 48, 48, 50, 52, 54, 54, 58, 64, 74, 82, 88, 94],35,30,40,),
    ([1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1],25,26,30,),
    ([2, 8, 8, 14, 15, 16, 17, 17, 18, 18, 24, 25, 25, 26, 36, 37, 39, 39, 40, 44, 46, 47, 51, 54, 56, 57, 57, 61, 61, 67, 68, 69, 72, 76, 77, 81, 82, 82, 82, 85, 85, 87, 94, 94, 98, 99],33,40,26,),
    ([-4, 84, 20, -84, -6, -78, 20, 56, 40, 0, 98, 80, -94, 36, -6, -98, 50, 66, -12, -58, -34, 68, -80, -30, -82, -76, -38, -60, 92, 94, 48, -84, 20, -66, -32, -92, 16, -96, -68, 94, -46, 30, 32, -34, 96, -92, -96, -86, -22],34,27,34,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],19,13,19,),
    ([71, 70, 13, 18, 70, 62, 88, 27, 17, 44, 89, 28, 74, 41, 20, 91, 95, 79, 40, 43, 38, 20, 5],21,22,22,)
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
