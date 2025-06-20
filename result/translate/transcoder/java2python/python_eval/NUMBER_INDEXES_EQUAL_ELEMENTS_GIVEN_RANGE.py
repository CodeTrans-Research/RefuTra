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
def f_gold ( a , n , l , r ) :
    count = 0
    for i in range ( l , r ) :
        if ( a [ i ] == a [ i + 1 ] ) :
            count += 1
    return count


def f_filled ( a , n , l , r ) :
    count = 0
    for i in range ( l , r ) :
        if a [ i ] == a [ i + 1 ] :
            count += 1
    return count

if __name__ == '__main__':
    param = [
    ([4, 13, 13, 16, 16, 19, 39, 41, 48, 52, 57, 62, 65, 67, 76, 84, 88, 91, 95, 96, 97, 98],18,12,17,),
    ([62, 76, 86, -8, 84, -6, 72, 84, 6, -50, -18, -94, 54, 90, -74, -64, -26, -14, -32, 62, 10, 4, 70, -28, 8, 18, 4, -62, -76, 84, -78, -4, 84, 98, 58, -68, 42, -6, 34, -38, 52, -84, 78],32,38,23,),
    ([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],10,6,6,),
    ([11, 75, 98, 29, 62, 53, 48, 91, 86, 66, 48, 94],8,6,6,),
    ([-94, -84, -70, -70, -40, -40, -36, -24, 10, 48, 62, 74],11,7,8,),
    ([1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0],36,40,37,),
    ([1, 2, 6, 7, 10, 11, 13, 19, 19, 25, 29, 30, 32, 34, 35, 45, 45, 46, 47, 48, 48, 53, 58, 61, 64, 65, 67, 75, 76, 81, 81, 84, 84, 85, 86, 94, 94, 96, 99],25,19,37,),
    ([-56, 42, -34, -12, -86, 82, -96, -66, 30, 16, -40, 72, 84, 94, -48, -30, 26, 50, 42, -44, -50, 22, -38, 8, 34, 94, 2, 16, -32, 18, -58, 12, -26, 28, -62],21,30,26,),
    ([0, 0, 0, 0, 1, 1, 1],4,5,5,),
    ([6, 29],1,1,1,)
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
