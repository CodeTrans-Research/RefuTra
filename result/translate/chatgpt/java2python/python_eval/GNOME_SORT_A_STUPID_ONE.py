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
    index = 0
    while index < n :
        if index == 0 :
            index = index + 1
        if arr [ index ] >= arr [ index - 1 ] :
            index = index + 1
        else :
            arr [ index ] , arr [ index - 1 ] = arr [ index - 1 ] , arr [ index ]
            index = index - 1
    return arr


def f_filled(arr, n):
    index = 0
    while index < n:
        if index == 0:
            index += 1
        if arr[index] >= arr[index - 1]:
            index += 1
        else:
            temp = arr[index]
            arr[index] = arr[index - 1]
            arr[index - 1] = temp
            index -= 1
    return

if __name__ == '__main__':
    param = [
    ([5, 20, 27, 28, 31, 31, 31, 34, 49, 55, 61, 63, 68, 69, 73, 78, 78, 82, 85, 87, 98],17,),
    ([34, -54, 0, 16, 66, -58, 88, -38, -94, -10],7,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],22,),
    ([10, 28, 65, 98, 25, 25, 77, 46, 77, 54, 16, 43, 52, 75, 9, 15, 1, 72, 56, 75, 73, 45, 5, 78, 11, 3, 93, 73, 31, 69, 8, 89, 44, 58, 64, 36, 7, 4],26,),
    ([-86, -50, -12, 26, 30, 68, 70, 80, 82],6,),
    ([1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0],17,),
    ([14, 28, 29, 31, 41, 59, 60, 62, 66, 67, 70, 70, 74, 76, 92, 96],13,),
    ([8, -22, 94, 28, 2, 14, 50, -54, 24, -26, -98, 58, -94, 4, -78, 98, 80, 72, -32, 58, -74],13,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],24,),
    ([3, 30, 84, 92, 29, 47, 36, 54, 93, 73, 53, 91, 81, 16, 51, 69, 82, 74, 80, 66, 77, 14, 85, 59, 86, 25, 85, 29, 19, 28, 13, 47, 61, 54, 13, 82, 52, 11, 10, 63, 52, 30, 35, 74],41,)
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
