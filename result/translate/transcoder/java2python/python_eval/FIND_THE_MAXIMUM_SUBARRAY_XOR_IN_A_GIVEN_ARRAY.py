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
    ans = - 2147483648
    for i in range ( n ) :
        curr_xor = 0
        for j in range ( i , n ) :
            curr_xor = curr_xor ^ arr [ j ]
            ans = max ( ans , curr_xor )
    return ans


def f_filled ( arr , n ) :
    ans = int ( '-1' )
    for i in range ( n ) :
        curr_xor = 0
        for j in range ( i , n ) :
            curr_xor = curr_xor ^ arr [ j ]
            ans = max ( ans , curr_xor )
    return ans

if __name__ == '__main__':
    param = [
    ([1, 7, 7, 11, 12, 18, 20, 23, 27, 30, 44, 47, 53, 53, 55, 57, 57, 58, 61, 62, 67, 74, 76, 80, 86, 86],13,),
    ([-34, -4, 68, -82, 54, 20, 6, -18, -70, 98, -40, 80, -28, 78, 28, 56, 26, 2, 2, -56, -66, 44, 0, -72, 12, 54, -40, 18, 28, -48, -56, 72, 84, 60, 76, 26, -8, 62],21,),
    ([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],12,),
    ([-2],1,),
    ([-92, -80, -76, -76, -74, -58, -44, -38, -34, -32, -30, -24, -20, -18, -4, -2, 2, 8, 44, 52, 52, 56, 70, 72, 80, 80, 98],15,),
    ([0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0],33,),
    ([1, 2, 3, 6, 9, 15, 15, 18, 19, 25, 31, 31, 33, 37, 39, 47, 49, 51, 51, 52, 52, 54, 58, 59, 59, 61, 62, 62, 65, 66, 66, 66, 66, 67, 71, 76, 77, 78, 79, 80, 83, 86, 87, 92, 97, 97, 98, 99],38,),
    ([34, -90, 64, 88, -46, -4, -96, 76, -32, 10, -8, -24, 32, -4, 86, -20, -86, -88, -72, 64, 12, 66, -96, -84, 16, -58, -48, 80, -80, 70, -94, -84, 56, 8, -14, 86, 72, -16, -18, 74, 40, 34, 20, 80],35,),
    ([1, 1],1,),
    ([57, 76, 2, 30, 24, 12, 49, 12, 5, 75, 55, 17, 62, 87, 21, 91, 88, 10, 20, 49, 46, 79, 51, 33, 94, 59, 48, 97, 70, 49],25,)
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
