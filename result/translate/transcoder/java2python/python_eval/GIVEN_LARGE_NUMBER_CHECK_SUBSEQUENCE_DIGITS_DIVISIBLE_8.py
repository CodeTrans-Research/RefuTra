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
def f_gold ( st ) :
    l = len ( st )
    arr = [ 0 ] * l
    for i in range ( 0 , l ) :
        for j in range ( i , l ) :
            for k in range ( j , l ) :
                if ( arr [ i ] % 8 == 0 ) :
                    return True
                elif ( ( arr [ i ] * 10 + arr [ j ] ) % 8 == 0 and i != j ) :
                    return True
                elif ( ( arr [ i ] * 100 + arr [ j ] * 10 + arr [ k ] ) % 8 == 0 and i != j and j != k and i != k ) :
                    return True
    return False


def f_filled ( str ) :
    i , j , k , l = len ( str ) , len ( str ) , len ( str ) , len ( str )
    arr = [ 0 for i in range ( l ) ]
    for i in range ( l ) :
        for j in range ( i , l ) :
            for k in range ( j , l ) :
                if arr [ i ] % 8 == 0 :
                    return True
                elif ( arr [ i ] * 10 + arr [ j ] ) % 8 == 0 and i != j :
                    return True
                elif ( arr [ i ] * 100 + arr [ j ] * 10 + arr [ k ] ) % 8 == 0 and i != j and j != k and i != k :
                    return True
    return False

if __name__ == '__main__':
    param = [
    ('1787075866',),
    ('8',),
    ('1110101110111',),
    ('6673177113',),
    ('7',),
    ('000001',),
    ('dbxMF',),
    ('71733',),
    ('01101101100',),
    ('',)
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
