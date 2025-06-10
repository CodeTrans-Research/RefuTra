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
def f_gold ( str ) :
    N = len ( str )
    cps = [ [ 0 for i in range ( N + 2 ) ] for j in range ( N + 2 ) ]
    for i in range ( N ) :
        cps [ i ] [ i ] = 1
    for L in range ( 2 , N + 1 ) :
        for i in range ( N ) :
            k = L + i - 1
            if ( k < N ) :
                if ( str [ i ] == str [ k ] ) :
                    cps [ i ] [ k ] = ( cps [ i ] [ k - 1 ] + cps [ i + 1 ] [ k ] + 1 )
                else :
                    cps [ i ] [ k ] = ( cps [ i ] [ k - 1 ] + cps [ i + 1 ] [ k ] - cps [ i + 1 ] [ k - 1 ] )
    return cps [ 0 ] [ N - 1 ]


def f_filled ( str ) :
    N = len ( str )
    cps = [ 1 for i in range ( N + 1 ) ]
    for L in range ( 2 , N + 1 ) :
        for i in range ( N ) :
            k = L + i - 1
            if k < N :
                if str [ i ] == str [ k ] :
                    cps [ i ] [ k ] = cps [ i ] [ k - 1 ] + cps [ i + 1 ] [ k ] + 1
                else :
                    cps [ i ] [ k ] = cps [ i ] [ k - 1 ] + cps [ i + 1 ] [ k ] - cps [ i + 1 ] [ k - 1 ]
    return cps [ 0 ] [ N - 1 ]

if __name__ == '__main__':
    param = [
    ('R',),
    ('2956350',),
    ('11100111110101',),
    ('TZTDLIIfAD',),
    ('98',),
    ('1100100001',),
    ('oKwGeatf',),
    ('19',),
    ('00010110100',),
    ('Cyq',)
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
