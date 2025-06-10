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
def f_gold ( N ) :
    if ( N <= 6 ) :
        return N
    screen = [ 0 ] * N
    for n in range ( 1 , 7 ) :
        screen [ n - 1 ] = n
    for n in range ( 7 , N + 1 ) :
        screen [ n - 1 ] = max ( 2 * screen [ n - 4 ] , max ( 3 * screen [ n - 5 ] , 4 * screen [ n - 6 ] ) ) ;
    return screen [ N - 1 ]


def f_filled ( N ) :
    if N <= 6 :
        return N
    screen = [ ]
    b = 0
    n = 0
    n=1 
    while n<7 :
        screen.append ( n )
        n += 1
    n=7 
    while n<N+1 :
        screen.append ( max ( 2 * screen [ n - 4 ] , max ( 3 * screen [ n - 5 ] , 4 * screen [ n - 6 ] ) ) )
        n += 1
    return screen [ N - 1 ]

if __name__ == '__main__':
    param = [
    (41,),
    (94,),
    (80,),
    (40,),
    (76,),
    (5,),
    (43,),
    (67,),
    (24,),
    (90,)
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
