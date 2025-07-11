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
    return sorted(arr[:n], reverse=False)[n-1]


def f_filled(arr, n):
        arr.sort()
        return arr[n - 1]

if __name__ == '__main__':
    param = [
    ([10, 12, 14, 16, 17, 17, 20, 24, 26, 28, 37, 38, 41, 45, 49, 50, 59, 61, 63, 65, 65, 66, 69, 70, 70, 73, 73, 74, 81, 81, 83, 87, 94, 97],17,),
    ([-56, 38, -22, 84, -60, 2, 68, -78, 62, -98, 24, 26, 48, 62, -80, -14, -84, 12, -54, -12, -20, -82, 10, -34, -50, -72, 78, 16, 30, -76, 72, 34, 6, 52, 44, 18, -38, 48, -14],25,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],11,),
    ([92, 5, 40, 65, 86, 51, 14, 29, 66, 6, 62, 92, 29, 13, 88, 54, 15, 60, 45, 2, 51, 9, 33, 51, 31, 11, 62, 61, 77, 38, 11, 4, 27, 54, 72, 64, 85, 46, 24, 44, 39, 73, 82, 85],40,),
    ([-92, -90, -84, -80, -80, -76, -70, -70, -48, -44, -38, -28, -14, -14, -12, -2, 2, 4, 6, 10, 16, 16, 20, 22, 24, 26, 50, 52, 56, 56, 58, 58, 74, 80, 82, 84, 86],33,),
    ([0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0],29,),
    ([5, 19, 20, 26, 31, 32, 34, 37, 39, 40, 46, 46, 50, 53, 58, 58, 59, 65, 72, 72, 75, 76, 77, 78, 81, 83, 83, 95, 98, 99],28,),
    ([32, -84, -84, 86, -24, 36, -12, 82, 48, -12, 82, -76, 84, -20, -12, -18, 46, -74, -14, -86],14,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],33,),
    ([95, 73, 74, 14, 73, 74, 19, 93, 34, 53, 85, 75, 80, 15, 36, 57, 15, 98, 51, 37, 8, 9, 62, 71, 28, 24, 37, 53, 84, 76, 22, 48, 15, 19, 43, 88, 58, 38, 63, 68, 27, 22, 37, 76, 59, 66, 22],34,)
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
