import sys
import math
import heapq
from queue import Queue# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( arr , n ) :
    diff = 10 ** 20
    for i in range ( n - 1 ) :
        for j in range ( i + 1 , n ) :
            if abs ( arr [ i ] - arr [ j ] ) < diff :
                diff = abs ( arr [ i ] - arr [ j ] )
    return diff


def f_filled(arr, n):
        diff = float('inf')
        for i in range(n - 1):
            for j in range(i + 1, n):
                if abs(arr[i] - arr[j]) < diff:
                    diff = abs(arr[i] - arr[j])
        return diff

if __name__ == '__main__':
    param = [
    ([1, 1, 2, 3, 5, 8, 10, 11, 15, 15, 16, 20, 26, 28, 30, 30, 33, 33, 39, 50, 50, 50, 54, 62, 66, 68, 69, 69, 74, 74, 75, 75, 76, 78, 82, 83, 85, 86, 86, 89, 89, 91, 91, 92, 92, 92, 93, 94, 98],32,),
    ([6, 6, -20, 88, -78, -18, 74, 72, 80, 76, -62, 38],11,),
    ([0, 1, 1, 1, 1],3,),
    ([75, 85, 49, 66, 44, 89, 80, 39, 64, 70, 25, 21, 81, 33, 90, 68, 51],16,),
    ([-96, -10, 0, 4, 54, 64],3,),
    ([1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0],41,),
    ([3, 3, 5, 5, 7, 7, 9, 11, 11, 18, 18, 18, 20, 29, 29, 31, 31, 32, 37, 43, 44, 46, 48, 50, 52, 52, 53, 63, 63, 65, 69, 72, 76, 76, 81, 84, 85, 86, 87, 87, 90, 94, 97, 97],27,),
    ([40, -46, 72, -28, 8, 90, 86, -90, 8, -66, -98, 6, 42, 86, 88, 42, -50, 74, -34, -16, -94, -56, -18, -18, 84, -44, 34, 80, 96, 42, -50, -92, 70, 80, 62, -38, -4, 68, 54, -14, 30, -18, -58],33,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],26,),
    ([15, 41, 32, 19, 68, 36, 61, 59, 5, 91, 53, 95, 10, 64, 15, 32, 14, 64, 48, 70, 85, 19, 83, 2, 33, 58, 93, 88, 21, 88, 45, 45, 18, 8],24,)
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
