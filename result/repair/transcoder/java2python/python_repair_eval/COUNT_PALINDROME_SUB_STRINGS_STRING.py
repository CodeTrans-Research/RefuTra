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
def f_gold ( str , n ) :
    dp = [ [ 0 for x in range ( n ) ] for y in range ( n ) ]
    P = [ [ False for x in range ( n ) ] for y in range ( n ) ]
    for i in range ( n ) :
        P [ i ] [ i ] = True
    for i in range ( n - 1 ) :
        if ( str [ i ] == str [ i + 1 ] ) :
            P [ i ] [ i + 1 ] = True
            dp [ i ] [ i + 1 ] = 1
    for gap in range ( 2 , n ) :
        for i in range ( n - gap ) :
            j = gap + i ;
            if ( str [ i ] == str [ j ] and P [ i + 1 ] [ j - 1 ] ) :
                P [ i ] [ j ] = True
            if ( P [ i ] [ j ] == True ) :
                dp [ i ] [ j ] = ( dp [ i ] [ j - 1 ] + dp [ i + 1 ] [ j ] + 1 - dp [ i + 1 ] [ j - 1 ] )
            else :
                dp [ i ] [ j ] = ( dp [ i ] [ j - 1 ] + dp [ i + 1 ] [ j ] - dp [ i + 1 ] [ j - 1 ] )
    return dp [ 0 ] [ n - 1 ]


def f_filled ( str , n ) :
    dp = [[0 for _ in range(n)] for _ in range(n)]
    P = [[0 for _ in range(n)] for _ in range(n)]
    for i in range ( n ) :
        P [ i ] [ i ] = True
    for i in range ( n - 1 ) :
        if str [ i ] == str [ i + 1 ] :
            P [ i ] [ i + 1 ] = True
            dp [ i ] [ i + 1 ] = 1
    for gap in range ( 2 , n ) :
        for i in range ( n - gap ) :
            j = gap + i
            if str [ i ] == str [ j ] and P [ i + 1 ] [ j - 1 ] :
                P [ i ] [ j ] = True
            if P [ i ] [ j ] == True :
                dp [ i ] [ j ] = dp [ i ] [ j - 1 ] + dp [ i + 1 ] [ j ] + 1 - dp [ i + 1 ] [ j - 1 ]
            else :
                dp [ i ] [ j ] = dp [ i ] [ j - 1 ] + dp [ i + 1 ] [ j ] - dp [ i + 1 ] [ j - 1 ]
    return dp [ 0 ] [ n - 1 ]

if __name__ == '__main__':
    param = [
    (['E', 'E', 'J', 'P', 'T', 'U', 'X', 'Y', 'Z', 'e', 'f', 'h', 'l', 'm', 'n', 'o', 'z'],11,),
    (['8', '7', '3', '4', '9', '5', '3', '1', '4', '0', '6', '8', '2', '5', '8', '3', '5', '2', '8', '6', '6', '3', '5', '7', '5', '5', '3', '7'],27,),
    (['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],23,),
    (['f', 'E', 'e', 'z', 'B', 'o', 'i', 'v', 'K', 'u', 'P', 'C', 'z', 'f', 'k', 'J', 't', 'R', 't', 'A', 'f', 'G', 'D', 'X', 'H', 'e', 'p', 'l', 'l', 'k', 'Z', 'Y', 'u', 'g', 'H', 'C', 'f', 'J', 'H', 'W'],27,),
    (['0', '0', '0', '1', '1', '1', '1', '1', '1', '2', '2', '2', '3', '3', '3', '3', '3', '4', '4', '4', '4', '4', '4', '5', '5', '5', '5', '6', '6', '7', '7', '9', '9', '9', '9', '9', '9'],35,),
    (['1', '0', '1', '1', '0', '0', '1', '1', '1', '0', '1', '0', '1', '1', '0', '1', '0', '1', '1', '1', '1', '1', '0', '1', '1', '0', '1', '0', '1', '1', '0', '0', '1', '0', '1', '0', '0', '0', '0', '0', '1', '1', '0', '1', '0', '1'],43,),
    (['C', 'C', 'D', 'F', 'L', 'M', 'P', 'X', 'a', 'f', 'i', 'j', 'w'],9,),
    (['7', '9', '0', '2', '8', '0', '7', '5', '9', '4', '5', '4', '8', '1', '9', '5', '3', '2', '4', '1', '2'],16,),
    (['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],32,),
    (['m', 'X', 'N', 'M'],3,)
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
