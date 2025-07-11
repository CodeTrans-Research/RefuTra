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
def f_gold ( high , low , n ) :
    if ( n <= 0 ) :
        return 0
    return max ( high [ n - 1 ] + f_gold ( high , low , ( n - 2 ) ) , low [ n - 1 ] + f_gold ( high , low , ( n - 1 ) ) ) ;


def f_filled ( high , low , n ) :
    if n <= 0 :
        return 0
    return max ( high [ n - 1 ] + f_filled ( high , low , ( n - 2 ) ) , low [ n - 1 ] + f_filled ( high , low , ( n - 1 ) ) )

if __name__ == '__main__':
    param = [
    ([1, 3, 9, 10, 13, 14, 15, 15, 17, 22, 23, 28, 30, 31, 37, 42, 45, 62, 62, 68, 68, 68, 78, 79, 82, 84, 87, 90, 99],[5, 10, 11, 14, 16, 22, 24, 30, 34, 35, 37, 37, 39, 41, 42, 42, 43, 55, 57, 63, 71, 76, 83, 83, 85, 90, 91, 97, 99],18,),
    ([-78, -12, 26, 80, 50, 4, -80, 86, 12, -2, 18, -50, -90, 56, -50, 88, -62, 96, -44, -82, 56],[-44, -14, 14, 0, 30, 78, 40, -12, -44, -16, 60, -12, -50, -66, 70, -98, -56, 48, -82, 94, 14],16,),
    ([1],[1],0,),
    ([21, 28, 13, 48, 26, 49, 16, 70, 81, 35, 74, 12, 97, 61, 10, 84, 94, 78, 40, 30, 30, 84, 41, 4, 95, 79, 38, 29, 9],[49, 88, 25, 93, 24, 56, 47, 44, 33, 27, 86, 57, 21, 25, 64, 44, 37, 99, 36, 54, 17, 29, 37, 17, 26, 43, 61, 27, 21],25,),
    ([-80, -36, -32, -20, -14, -12, 10, 12, 72],[-76, -54, -50, -28, 0, 58, 70, 78, 90],4,),
    ([1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],[0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1],24,),
    ([1, 7, 9, 10, 13, 14, 15, 20, 23, 24, 24, 24, 26, 27, 29, 31, 32, 33, 34, 35, 46, 48, 49, 51, 51, 53, 53, 56, 56, 60, 62, 64, 64, 70, 73, 73, 73, 74, 77, 78, 79, 79, 79, 80, 86, 89, 89, 92, 98],[1, 3, 3, 4, 8, 8, 10, 10, 10, 12, 12, 15, 15, 22, 23, 28, 28, 30, 31, 33, 34, 35, 36, 36, 36, 42, 44, 44, 51, 54, 57, 58, 59, 59, 63, 65, 66, 68, 69, 71, 73, 76, 77, 78, 79, 79, 86, 87, 93],31,),
    ([56, 48, 40, -56, 44, -86, -28, -32, -34, 4, -94, -14, 28, -74],[82, -40, -16, -64, 12, -6, 60, 48, -58, -4, 42, -28, 24, -58],8,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],16,),
    ([85, 13, 35, 57, 8, 48, 65, 54, 88, 7, 66, 30, 47, 51],[1, 42, 42, 89, 3, 21, 49, 98, 4, 59, 26, 85, 53, 34],8,)
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
