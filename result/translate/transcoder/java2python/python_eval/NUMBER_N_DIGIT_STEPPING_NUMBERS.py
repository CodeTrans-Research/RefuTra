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
def f_gold ( n ) :
    dp = [ [ 0 for x in range ( 10 ) ] for y in range ( n + 1 ) ] ;
    if ( n == 1 ) :
        return 10 ;
    for j in range ( 10 ) :
        dp [ 1 ] [ j ] = 1 ;
    for i in range ( 2 , n + 1 ) :
        for j in range ( 10 ) :
            if ( j == 0 ) :
                dp [ i ] [ j ] = dp [ i - 1 ] [ j + 1 ] ;
            elif ( j == 9 ) :
                dp [ i ] [ j ] = dp [ i - 1 ] [ j - 1 ] ;
            else :
                dp [ i ] [ j ] = ( dp [ i - 1 ] [ j - 1 ] + dp [ i - 1 ] [ j + 1 ] ) ;
    sum = 0 ;
    for j in range ( 1 , 10 ) :
        sum = sum + dp [ n ] [ j ] ;
    return sum ;


def f_filled ( n ) :
    dp = [ 0 ] * ( n + 1 )
    if n == 1 :
        return 10
    for j in range ( 0 , 9 ) :
        dp [ 1 ] [ j ] = 1
    for i in range ( 2 , n + 1 ) :
        for j in range ( 0 , 9 ) :
            if j == 0 :
                dp [ i ] [ j ] = dp [ i - 1 ] [ j + 1 ]
            elif j == 9 :
                dp [ i ] [ j ] = dp [ i - 1 ] [ j - 1 ]
            else :
                dp [ i ] [ j ] = dp [ i - 1 ] [ j - 1 ] + dp [ i - 1 ] [ j + 1 ]
    sum = 0
    for j in range ( 1 , 9 ) :
        sum += dp [ n ] [ j ]
    return sum

if __name__ == '__main__':
    param = [
    (18,),
    (16,),
    (13,),
    (10,),
    (26,),
    (11,),
    (20,),
    (25,),
    (12,),
    (13,)
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

