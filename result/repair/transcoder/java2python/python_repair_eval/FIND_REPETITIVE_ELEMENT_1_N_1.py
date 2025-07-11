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
    return sum ( arr [ : n ] ) - ( ( ( n - 1 ) * n ) // 2 )


def f_filled ( arr , n ) :
    sum = 0
    for i in range ( n ) :
        sum += arr [ i ]
    return sum - ( ( ( n - 1 ) * n ) // 2 )

if __name__ == '__main__':
    param = [
    ([4, 8, 27, 34, 39, 42, 43, 54, 72],5,),
    ([-38, -66, -38, -48, -96, 74, -32, -62, -34, -32, -88, -12, -8, -4],9,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],8,),
    ([88, 86, 23, 81, 76, 16, 94, 64, 59, 50, 71, 62, 10, 89, 73, 64, 65, 96, 83, 40, 99, 40, 77, 33, 14, 62, 6, 89, 74, 96, 93, 29, 15, 93, 9, 58, 98, 76, 23, 23, 70, 99],31,),
    ([-96, -94, -82, -64, -56, -40, -36, -34, -32, -24, -24, -22, -20, -20, -20, -18, -18, -12, -10, -6, 16, 20, 20, 22, 26, 30, 36, 46, 46, 50, 50, 52, 64, 64, 64, 68, 72, 74, 76, 92, 96, 98],28,),
    ([0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1],25,),
    ([2, 6, 7, 13, 19, 23, 37, 39, 42, 42, 43, 45, 52, 53, 55, 56, 59, 63, 66, 71, 76, 85, 86, 89, 92, 94, 96, 99],27,),
    ([52, -56, -12, 78, 6, 32, 0, 36, 34, -54, -74, -32],11,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],15,),
    ([10, 42, 50, 5, 74, 81, 30, 76, 6, 34, 86, 4, 77, 71, 96, 22, 34, 50, 35, 16, 60, 11, 21, 38],13,)
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
