import sys
import math
import heapq
from queue import Queue# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( arr , N ) :
    arr = arr [ : N ]
    if N < 3 :
        return False
    arr.sort ( )
    for i in range ( N - 2 ) :
        if arr [ i ] + arr [ i + 1 ] > arr [ i + 2 ] :
            return True
    return False


def f_filled(arr, N):
        arr = arr[:N]
        arr.sort()
        for i in range(N - 2):
            if arr[i] + arr[i + 1] > arr[i + 2]:
                return True
        return False

if __name__ == '__main__':
    param = [
    ([2, 6, 8, 10, 14, 15, 16, 19, 21, 26, 26, 26, 28, 29, 30, 33, 33, 35, 36, 36, 41, 44, 45, 45, 45, 49, 51, 54, 57, 59, 61, 64, 68, 70, 70, 72, 73, 74, 76, 78, 87, 89, 89, 91, 92, 93, 94, 95, 97],25,),
    ([50, -58, -44, 90, 18, -26, -74, -46, 96, 32, 72, 46, -90, 86, -10, 82, -72, 86, -64, -96, -12, -14, -36, 16, 38, 56, 54, 10, 74, -86, -64, -56, 30, -50, 46, 4, 88, -94, -4, -78, 22, -78],23,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],10,),
    ([80, 24, 41, 90, 24, 95],4,),
    ([-90, -88, -84, -82, -82, -80, -70, -66, -62, -60, -60, -48, -46, -44, -42, -20, -16, -4, 18, 26, 28, 32, 36, 46, 60, 62, 68, 72, 78, 98],21,),
    ([0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0],25,),
    ([3, 9, 14, 16, 16, 26, 30, 31, 32, 37, 42, 42, 43, 49, 51, 56, 64, 69, 76, 77, 77, 79, 85, 88, 89, 91, 94, 95],19,),
    ([-60, -90, -30, -42, 80, -66, 94, 60, -68, -74, -50, 42, -38, -34, -84, -58, 30, 98, -52, 6, -60, -60],11,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],18,),
    ([24, 80, 16, 31, 5, 31, 66, 1, 13, 77, 88, 40, 34, 15, 90, 46, 8, 26, 39, 52, 22, 33, 3, 30, 49, 51, 69, 50, 39, 59],23,)
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

