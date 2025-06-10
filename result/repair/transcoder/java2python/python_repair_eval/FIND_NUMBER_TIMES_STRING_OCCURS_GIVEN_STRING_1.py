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
def f_gold ( a , b ) :
    m = len ( a )
    n = len ( b )
    lookup = [ [ 0 ] * ( n + 1 ) for i in range ( m + 1 ) ]
    for i in range ( n + 1 ) :
        lookup [ 0 ] [ i ] = 0
    for i in range ( m + 1 ) :
        lookup [ i ] [ 0 ] = 1
    for i in range ( 1 , m + 1 ) :
        for j in range ( 1 , n + 1 ) :
            if a [ i - 1 ] == b [ j - 1 ] :
                lookup [ i ] [ j ] = lookup [ i - 1 ] [ j - 1 ] + lookup [ i - 1 ] [ j ]
            else :
                lookup [ i ] [ j ] = lookup [ i - 1 ] [ j ]
    return lookup [ m ] [ n ]


def f_filled ( a , b ) :
    m = len ( a )
    n = len ( b )
    lookup = [[0 for _ in range(n+1)] for _ in range(m+1)]
    i=0 
    while i<n+1 :
        lookup [ 0 ] [ i ] = 0
        i += 1
    i=0 
    while i<m+1 :
        lookup [ i ] [ 0 ] = 1
        i += 1
    i=1 
    while i<m+1 :
        j=1 
        while j<n+1 :
            if a [ i - 1 ] == b [ j - 1 ] :
                lookup [ i ] [ j ] = lookup [ i - 1 ] [ j - 1 ] + lookup [ i - 1 ] [ j ]
            else :
                lookup [ i ] [ j ] = lookup [ i - 1 ] [ j ]
            j += 1
        i += 1
    return lookup [ m ] [ n ]

if __name__ == '__main__':
    param = [
    ('fZOKCdZ Lav','fKA',),
    ('2','187012',),
    ('1000001110','0',),
    ('IAOyBzgIWHo','oA',),
    ('211806','10',),
    ('1','001011100',),
    ('CVaQTG','CT',),
    ('6265187228','628',),
    ('10111101101000','01111',),
    ('vEi','bigsvkQG',)
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
