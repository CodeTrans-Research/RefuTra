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
    min_xor = 999999
    val = 0
    for i in range ( 0 , n ) :
        for j in range ( i + 1 , n ) :
            val = arr [ i ] ^ arr [ j ]
            min_xor = min ( min_xor , val )
    return min_xor


def f_filled(arr, n):
    min_xor = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            min_xor = min(min_xor, arr[i] ^ arr[j])
    return min_xor

if __name__ == '__main__':
    param = [
    ([4, 5, 7, 10, 10, 11, 14, 19, 21, 24, 27, 27, 27, 28, 28, 28, 33, 34, 41, 42, 43, 48, 52, 53, 53, 59, 62, 64, 66, 71, 77, 78, 78, 79, 80, 82, 90, 97, 99, 99],34,),
    ([-68, -58, 52, 88, 90, 66, -66, -84, -70, -64, 56, 42, 94, -10, 0, 80, 8, 28, -94, 36, 90, 56, 56, 80, -94, 50, 90, -28, -22, -2, -96, 74, -16, -14],17,),
    ([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],9,),
    ([57, 63, 11, 73, 60, 73, 25, 65, 39, 48, 31, 17, 23, 94, 10, 97, 42, 45, 83, 75, 97, 96],21,),
    ([-92, -92, -90, -88, -84, -82, -66, -64, -64, -62, -44, -42, -40, -28, -22, -12, -4, -2, 0, 4, 16, 22, 28, 34, 54, 60, 72, 74, 78, 86, 94],18,),
    ([1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0],36,),
    ([2, 2, 6, 13, 16, 16, 17, 19, 19, 20, 22, 25, 27, 29, 34, 34, 34, 36, 38, 39, 42, 49, 49, 53, 59, 59, 71, 77, 79, 82, 83, 83, 84, 84, 86, 86, 87, 88, 93, 96],36,),
    ([-14, 20, 36, 12, -54, -50, 92, -28, 44, -46, 6, 96, 82, 70, -20, 24, -96, -14, 46, -28, -46, -28, 22, -82, 36, -94, -48, -92, 96, 74, 14],20,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],39,),
    ([50, 48, 94, 64, 60, 48, 79, 75, 77, 62, 33, 42, 22, 78, 32, 99, 27, 23, 76, 51, 34, 54, 70, 12, 19, 17, 13, 82, 96, 70, 4, 12, 5, 11, 23, 23, 18, 93, 38, 69],30,)
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

