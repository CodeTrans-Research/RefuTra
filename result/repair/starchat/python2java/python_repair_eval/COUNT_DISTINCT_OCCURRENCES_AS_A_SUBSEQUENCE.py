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
def f_gold ( S , T ) :
    m = len ( T )
    n = len ( S )
    if m > n :
        return 0
    mat = [ [ 0 for _ in range ( n + 1 ) ] for __ in range ( m + 1 ) ]
    for i in range ( 1 , m + 1 ) :
        mat [ i ] [ 0 ] = 0
    for j in range ( n + 1 ) :
        mat [ 0 ] [ j ] = 1
    for i in range ( 1 , m + 1 ) :
        for j in range ( 1 , n + 1 ) :
            if T [ i - 1 ] != S [ j - 1 ] :
                mat [ i ] [ j ] = mat [ i ] [ j - 1 ]
            else :
                mat [ i ] [ j ] = ( mat [ i ] [ j - 1 ] + mat [ i - 1 ] [ j - 1 ] )
    return mat [ m ] [ n ]


def f_filled(S, T):
        m = len(T)
        n = len(S)
        if m > n:
            return 0
        mat = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            mat[i][0] = 0
        j=0 
        while j<n+1 :
            mat[0][j] = 1
            j += 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if T[i - 1]!= S[j - 1]:
                    mat[i][j] = mat[i][j - 1]
                else:
                    mat[i][j] = mat[i][j - 1] + mat[i - 1][j - 1]
        return mat[m][n]

if __name__ == '__main__':
    param = [
    ('banana','ban',),
    ('49597223','42',),
    ('1000010000011','010',),
    ('BTlzufK','EpsVuzP lf',),
    ('3474007','370',),
    ('0010','00000',),
    ('dKHhoTD','doT',),
    ('9123259723','123',),
    ('11001000111110','0',),
    ('iY WJlIZ','iI',)
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
