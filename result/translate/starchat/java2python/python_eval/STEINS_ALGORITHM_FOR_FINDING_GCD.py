import sys
import math
import heapq
from queue import Queue# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( a , b ) :
    if ( a == 0 ) :
        return b
    if ( b == 0 ) :
        return a
    k = 0
    while ( ( ( a | b ) & 1 ) == 0 ) :
        a = a >> 1
        b = b >> 1
        k = k + 1
    while ( ( a & 1 ) == 0 ) :
        a = a >> 1
    while ( b != 0 ) :
        while ( ( b & 1 ) == 0 ) :
            b = b >> 1
        if ( a > b ) :
            temp = a
            a = b
            b = temp
        b = ( b - a )
    return ( a << k )


def f_filled(a, b):
        if a == 0:
            return b
        if b == 0:
            return a
        k = 0
        while ((a | b) & 1) == 0:
            k += 1
            a >>= 1
            b >>= 1
        while (a & 1) == 0:
            a >>= 1
        while (b & 1) == 0:
            b >>= 1
        while a > b:
            temp = a
            a = b
            b = temp
        return a << k

if __name__ == '__main__':
    param = [
    (37,93,),
    (58,13,),
    (89,27,),
    (75,14,),
    (59,47,),
    (84,39,),
    (47,76,),
    (37,75,),
    (83,62,),
    (28,58,)
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
