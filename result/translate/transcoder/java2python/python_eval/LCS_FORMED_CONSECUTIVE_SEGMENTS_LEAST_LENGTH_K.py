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
def f_gold ( k , s1 , s2 ) :
    n = len ( s1 )
    m = len ( s2 )
    lcs = [ [ 0 for x in range ( m + 1 ) ] for y in range ( n + 1 ) ]
    cnt = [ [ 0 for x in range ( m + 1 ) ] for y in range ( n + 1 ) ]
    for i in range ( 1 , n + 1 ) :
        for j in range ( 1 , m + 1 ) :
            lcs [ i ] [ j ] = max ( lcs [ i - 1 ] [ j ] , lcs [ i ] [ j - 1 ] )
            if ( s1 [ i - 1 ] == s2 [ j - 1 ] ) :
                cnt [ i ] [ j ] = cnt [ i - 1 ] [ j - 1 ] + 1 ;
            if ( cnt [ i ] [ j ] >= k ) :
                for a in range ( k , cnt [ i ] [ j ] + 1 ) :
                    lcs [ i ] [ j ] = max ( lcs [ i ] [ j ] , lcs [ i - a ] [ j - a ] + a )
    return lcs [ n ] [ m ]


def f_filled ( k , s1 , s2 ) :
    n = len ( s1 )
    m = len ( s2 )
    lcs = [ [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * n + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m + [ 0 ] * m

if __name__ == '__main__':
    param = [
    (4,'aggayxysdfa','aggajxaaasdfa',),
    (2,'55571659965107','390286654154',),
    (3,'01011011100','0000110001000',),
    (5,'aggasdfa','aggajasdfaxy',),
    (2,'5710246551','79032504084062',),
    (3,'0100010','10100000',),
    (3,'aabcaaaa','baaabcd',),
    (1,'1219','3337119582',),
    (2,'111000011','011',),
    (2,'wiC oD','csiuGOUwE',)
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
