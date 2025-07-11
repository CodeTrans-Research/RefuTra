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
    cum_sum = 0
    for i in range ( 0 , n ) :
        cum_sum += arr [ i ]
    curr_val = 0
    for i in range ( 0 , n ) :
        curr_val += i * arr [ i ]
    res = curr_val
    for i in range ( 1 , n ) :
        next_val = ( curr_val - ( cum_sum - arr [ i - 1 ] ) + arr [ i - 1 ] * ( n - 1 ) )
        curr_val = next_val
        res = max ( res , next_val )
    return res


def f_filled ( arr , n ) :
    cum_sum = 0
    for i in range ( n ) :
        cum_sum += arr [ i ]
    curr_val = 0
    for i in range ( n ) :
        curr_val += i * arr [ i ]
    res = curr_val
    for i in range ( 1 , n ) :
        next_val = curr_val - ( cum_sum - arr [ i - 1 ] ) + arr [ i - 1 ] * ( n - 1 )
        curr_val = next_val
        res = max ( res , next_val )
    return res

if __name__ == '__main__':
    param = [
    ([6, 6, 13, 14, 16, 20, 24, 24, 24, 27, 28, 36, 49, 51, 55, 56, 62, 69, 74, 74, 76, 85, 86, 90, 92, 98],13,),
    ([-42, 96, 68, 64, 14, -74, 76, 42, 34, -92, -20, 28, -80, -34, -22, 96, -46, 96, 10, -82, 82, 50, -24, 48, 56, 72, -40, -86, 84, 66, -62, 50, -76, 34],27,),
    ([0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],10,),
    ([37, 88, 70, 86, 24, 62, 34, 44, 37, 42, 46, 34, 23, 32, 55, 2, 5, 70, 30, 46, 40, 65, 91, 4, 7, 74, 46, 12, 30, 22, 1, 91, 89, 88, 97, 6, 6, 11, 33, 14, 68, 24],39,),
    ([-92, -90, -70, -70, -10, 2, 10, 12, 14, 40, 44, 46, 64, 68, 68, 96],11,),
    ([1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1],15,),
    ([9, 15, 15, 17, 19, 20, 21, 23, 25, 25, 25, 32, 32, 33, 45, 51, 54, 59, 68, 71, 71, 71, 72, 75, 78, 80, 82, 82, 88, 89, 92, 93, 94, 97],22,),
    ([52, -78, -80, 32, -56, -98, -36, 86, 34, -36, 42, 46, 50, 0, 34, -46, -2, -18, -96, 12, -42, 62, 32, 78, 66, -8, 50, 60, 10, -18, 66, 80, -24, -98, 8, 48, 34, 44, -80, -34, 72, 0, -60, 52, 40, 20],45,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],33,),
    ([45, 35, 25, 7, 24, 73, 25, 86, 48, 70, 47, 91, 96, 15, 39, 9],8,)
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
