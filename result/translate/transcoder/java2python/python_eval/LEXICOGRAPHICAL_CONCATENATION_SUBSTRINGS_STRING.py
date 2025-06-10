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
def f_gold ( s ) :
    n = len ( s ) ;
    sub_count = ( n * ( n + 1 ) ) // 2 ;
    arr = [ 0 ] * sub_count ;
    index = 0 ;
    for i in range ( n ) :
        for j in range ( 1 , n - i + 1 ) :
            arr [ index ] = s [ i : i + j ] ;
            index += 1 ;
    arr.sort ( ) ;
    res = "" ;
    for i in range ( sub_count ) :
        res += arr [ i ] ;
    return res ;


def f_filled ( s ) :
    n = len ( s )
    sub_count = n * ( n + 1 ) // 2
    arr = [ ]
    index = 0
    for i in range ( n ) :
        for len in range ( 1 , n - i + 1 ) :
            arr.append ( s [ i : i + len ] )
    arr.sort ( )
    res = ""
    for i in range ( sub_count ) :
        res += arr [ i ]
    return res

if __name__ == '__main__':
    param = [
    ('sqGOi',),
    ('848580',),
    ('01001110011001',),
    ('ZhWXUKmeiI',),
    ('0917296541285',),
    ('01101001111100',),
    ('tjP kR',),
    ('999907',),
    ('011100',),
    ('qJPHNSJOUj',)
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
