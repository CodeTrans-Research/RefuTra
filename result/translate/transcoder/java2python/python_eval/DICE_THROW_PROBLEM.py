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
def f_gold ( m , n , x ) :
    table = [ [ 0 ] * ( x + 1 ) for i in range ( n + 1 ) ]
    for j in range ( 1 , min ( m + 1 , x + 1 ) ) :
        table [ 1 ] [ j ] = 1
    for i in range ( 2 , n + 1 ) :
        for j in range ( 1 , x + 1 ) :
            for k in range ( 1 , min ( m + 1 , j ) ) :
                table [ i ] [ j ] += table [ i - 1 ] [ j - k ]
    return table [ - 1 ] [ - 1 ]


def f_filled ( m , n , x ) :
    table = [ [ 0 ] * ( n + 1 ) + [ x + 1 ] * ( n + 1 ) for j in range ( 1 , m + 1 ) ]
    for i in range ( 2 , n + 1 ) :
        for j in range ( 1 , x + 1 ) :
            for k in range ( 1 , j + 1 ) and k <= m :
                table [ i ] [ j ] += table [ i - 1 ] [ j - k ]
    return table [ n ] [ x ]

if __name__ == '__main__':
    param = [
    (94,4,69,),
    (7,12,33,),
    (20,44,24,),
    (90,94,88,),
    (50,58,27,),
    (32,90,29,),
    (46,25,6,),
    (82,50,87,),
    (43,82,70,),
    (6,83,19,)
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
