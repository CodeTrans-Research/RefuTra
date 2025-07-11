import sys
import math
import heapq
from queue import Queue# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( arr , n , key , capacity ) :
    if ( n >= capacity ) :
        return n
    i = n - 1
    while i >= 0 and arr [ i ] > key :
        arr [ i + 1 ] = arr [ i ]
        i -= 1
    arr [ i + 1 ] = key
    return ( n + 1 )


def f_filled(arr, n, key, capacity):
        if n >= capacity:
            return n
        i = n - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key
        return n + 1

if __name__ == '__main__':
    param = [
    ([69],0,0,0,),
    ([-34, -38, -72, 90, -84, -40, -40, -52, -12, 80, -4, -58],6,6,9,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],13,19,11,),
    ([96, 34, 11, 1, 36, 79, 64, 75, 75, 96, 32, 18, 25, 79, 63, 80, 90, 75, 44, 71, 48, 1, 62, 53, 17, 98],21,20,13,),
    ([-98, -92, -92, -84, -82, -80, -80, -74, -70, -60, -48, -42, -36, -34, -34, -34, -30, -28, -16, -6, -2, -2, 2, 12, 14, 20, 24, 40, 46, 50, 60, 66, 70, 72, 78, 82, 88, 92, 94, 94, 96],30,32,28,),
    ([1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0],12,9,10,),
    ([10, 12, 12, 19, 20, 21, 24, 27, 37, 47, 50, 54, 55, 58, 61, 63, 63, 68, 73, 75, 87, 90, 90, 92, 92],12,13,21,),
    ([-74, 62, 74, 92, -38, -28, -26, 4, 88, -68, -76, -20, -4, 12, 72, 6, 42, 36, 88, -96, -80, 90, 80, -26, -36, -72, -62, 38, -20, 40, -10, -22, -20, 38, 82, -84, 8, -60, 86, -26, 44, -72, -70, -16, -22, 18, -16, 76, -50],37,26,42,),
    ([1, 1, 1, 1, 1],3,4,2,),
    ([64, 80, 47, 58, 41, 3, 85, 96, 51, 4, 22, 89, 67, 54, 88, 15, 83, 31, 19, 28, 40, 67, 37, 13, 63, 38, 27, 14, 7, 68],23,24,25,)
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
