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
def f_gold ( arr , n ) :
    Hash = dict ( )
    for i in range ( n ) :
        if arr [ i ] in Hash.keys ( ) :
            Hash [ arr [ i ] ] += 1
        else :
            Hash [ arr [ i ] ] = 1
    max_count = 0
    res = - 1
    for i in Hash :
        if ( max_count < Hash [ i ] ) :
            res = i
            max_count = Hash [ i ]
    return res


def f_filled(arr, n):
    hp = {}
    
    for i in range(n):
        key = arr[i]
        if key in hp:
            freq = hp[key]
            freq += 1
            hp[key] = freq
        else:
            hp[key] = 1
    
    max_count = 0
    res = -1
    
    for key, value in hp.items():
        if max_count < value:
            res = key
            max_count = value
    
    return res

if __name__ == '__main__':
    param = [
    ([3, 5, 7, 9, 9, 10, 11, 15, 19, 19, 29, 31, 34, 34, 35, 37, 41, 43, 45, 47, 51, 51, 55, 57, 59, 61, 65, 67, 73, 76, 77, 77, 80, 83, 83, 84, 84, 92, 94],24,),
    ([14, -38, -84, 24, 82, -68, 60, 2, -22, 54, 90, 90, -38, -8, -72, 68, 50, 54, -32, -66, -10, -70, -28, 18, 58, -54, -30, 60, -24, -48, 22, 32, -18, 2, -64, -56, 70, -92, -38, -70, 22, -36, -64],28,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],18,),
    ([76, 18, 41, 46, 34, 41, 56, 76, 14, 82, 51, 87, 1, 92, 9, 2, 68, 82, 43, 98, 88, 62, 84, 25, 7, 87, 37, 7, 55, 98, 60, 99, 92, 56, 17, 82, 28, 43, 40, 1, 99, 79, 38, 75, 84, 61, 21, 11],37,),
    ([-92, -86, -86, -84, -70, -68, -68, -66, -62, -52, -52, -50, -48, -38, -22, -14, -6, 4, 8, 10, 10, 16, 22, 36, 38, 40, 50, 50, 70, 78, 80, 86, 96, 96, 98],21,),
    ([1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0],18,),
    ([3, 53, 56, 57, 66, 73, 76, 94, 97],8,),
    ([12, 60, -94, 92],3,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],21,),
    ([95, 93, 82, 73, 61, 24, 73, 21, 47, 91, 48, 42, 76, 12, 89, 21, 3, 30, 5, 49, 26, 54, 16, 70, 50, 21, 58, 36, 16],25,)
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
