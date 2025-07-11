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
def f_gold ( poly , n , x ) :
    result = poly [ 0 ]
    for i in range ( 1 , n ) :
        result = result * x + poly [ i ]
    return result


def f_filled(poly, n, x):
    result = poly[0]
    for i in range(1, n):
        result = result * x + poly[i]
    return result

if __name__ == '__main__':
    param = [
    ([3, 18, 22, 27, 31, 33, 36, 36, 37, 37, 40, 48, 49, 49, 50, 58, 66, 71, 75, 85, 89, 91],16,16,),
    ([42, -88, 28, 8, 30, -8, -16, 86, 50, 84, 12, -20, -70, -40, -54, -76, 84, 90, -40, -68, -40, 36, -34, 14, 94, -44, 70, 58, -48, -72, 14, -70, 32],31,20,),
    ([0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],10,8,),
    ([66, 72, 27, 72, 71, 75, 94, 49, 47, 21, 21, 71, 84, 61, 14, 20, 5, 31, 62, 12, 56, 56, 12, 66, 26, 68, 30, 98, 20],15,26,),
    ([-96, -96, -94, -82, -72, -54, -54, -46, -34, -30, -28, -18, -2, 2, 6, 8, 10, 16, 18, 24, 26, 28, 44, 48, 48, 52, 56, 58, 58, 70, 70, 82, 84, 88, 94],25,34,),
    ([0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1],20,25,),
    ([2, 3, 8, 13, 15, 17, 18, 18, 25, 29, 29, 31, 36, 37, 42, 42, 42, 51, 52, 52, 54, 54, 58, 64, 70, 70, 74, 75, 78, 80, 83, 85, 86, 88, 95, 96, 97, 98, 99],19,32,),
    ([-56, -12, -92, -48, -98, -80, -96, -42, -50, 74, 88, 20, 78, -74, -20, -32, -30, 58, -22, -16, 68, 72, -50, -72, 66, 72, 74, -98, -22, -40, -90, 88, 42, 24],29,23,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],20,23,),
    ([86, 62, 30, 27, 98, 75, 93, 37, 70, 16, 20, 74, 46, 74, 25, 59, 86, 32, 17, 90, 80, 10, 17],12,12,)
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
