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
    res = ord ( str [ 0 ] ) - 48
    for i in range ( 1 , len ( str ) ) :
        if ( str [ i ] == '0' or str [ i ] == '1' or res < 2 ) :
            res += ord ( str [ i ] ) - 48
        else :
            res += ord ( str [ i ] ) - 48
    return res


def f_filled ( str ) :
    res = str [ 0 ] - '0'
    for c in str [ 1 : ] :
        if c in [ '0' , '1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' ] :
            res += ( c - '0' )
        else :
            res += ( c - '0' )
    return res

if __name__ == '__main__':
    param = [
    ('pR',),
    ('9518',),
    ('1',),
    ('nNMCIXUCpRMmvO',),
    ('3170487',),
    ('0100101010',),
    ('Z rONcUqWb',),
    ('00419297',),
    ('00',),
    ('r',)
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
