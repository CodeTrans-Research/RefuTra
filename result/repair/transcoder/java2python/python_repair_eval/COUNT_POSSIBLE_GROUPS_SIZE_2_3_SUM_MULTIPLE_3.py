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
    c = [ 0 , 0 , 0 ]
    res = 0
    for i in range ( 0 , n ) :
        c [ arr [ i ] % 3 ] += 1
    res += ( ( c [ 0 ] * ( c [ 0 ] - 1 ) ) >> 1 )
    res += c [ 1 ] * c [ 2 ]
    res += ( c [ 0 ] * ( c [ 0 ] - 1 ) * ( c [ 0 ] - 2 ) ) // 6
    res += ( c [ 1 ] * ( c [ 1 ] - 1 ) * ( c [ 1 ] - 2 ) ) // 6
    res += ( ( c [ 2 ] * ( c [ 2 ] - 1 ) * ( c [ 2 ] - 2 ) ) // 6 )
    res += c [ 0 ] * c [ 1 ] * c [ 2 ]
    return res


def f_filled ( arr , n ) :
    c = [ 0 , 0 , 0 ]
    i = 0
    res = 0
    for i in range ( n ) :
        c [ arr [ i ] % 3 ] += 1
    res += ( ( c [ 0 ] * ( c [ 0 ] - 1 ) ) >> 1 )
    res += c [ 1 ] * c [ 2 ]
    res += ( c [ 0 ] * ( c [ 0 ] - 1 ) * ( c [ 0 ] - 2 ) ) // 6
    res += ( c [ 1 ] * ( c [ 1 ] - 1 ) * ( c [ 1 ] - 2 ) ) // 6
    res += ( ( c [ 2 ] * ( c [ 2 ] - 1 ) * ( c [ 2 ] - 2 ) ) // 6 )
    res += c [ 0 ] * c [ 1 ] * c [ 2 ]
    return res

if __name__ == '__main__':
    param = [
    ([1, 3, 6, 12, 18, 31, 36, 43, 47, 59, 64, 64, 69, 69, 94, 98, 98],12,),
    ([94, 46, 64, 18, 70, 22, -98, 52, -26, 34, -22, 22, 40, 66, -72, -66, 86, 84, 12, -38, 28, -60, -10, -30, -78, 76, 62, 74, 24, -64, 0, 92, -20, -66, -52],23,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],29,),
    ([68, 96, 74, 38, 70, 70],5,),
    ([-88, -74, -70, -64, -64, -64, -58, -52, -18, -10, -6, 4, 4, 28, 44, 48, 52, 54, 64, 72, 76, 94],18,),
    ([0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1],36,),
    ([9, 12, 14, 21, 27, 28, 45, 50, 54, 57, 58, 62, 78, 82, 91, 92, 95],9,),
    ([16, -46, -32, -36, -84, -14, -18, 16, 54, 90, -4],8,),
    ([0, 0, 1, 1],3,),
    ([53, 32, 54, 84, 79, 37, 44, 30, 92, 53, 89, 95],8,)
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
