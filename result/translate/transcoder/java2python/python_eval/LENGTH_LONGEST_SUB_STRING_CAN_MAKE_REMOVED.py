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
def f_gold ( S ) :
    arr = [ ]
    arr.append ( [ '@' , - 1 ] )
    maxlen = 0
    for i in range ( len ( S ) ) :
        arr.append ( [ S [ i ] , i ] )
        while ( len ( arr ) >= 3 and arr [ len ( arr ) - 3 ] [ 0 ] == '1' and arr [ len ( arr ) - 2 ] [ 0 ] == '0' and arr [ len ( arr ) - 1 ] [ 0 ] == '0' ) :
            arr.pop ( )
            arr.pop ( )
            arr.pop ( )
        tmp = arr [ - 1 ]
        maxlen = max ( maxlen , i - tmp [ 1 ] )
    return maxlen


def f_filled ( str ) :
    arr = [ ( '@' , - 1 ) ]
    maxlen = 0
    for i in range ( len ( str ) ) :
        arr.append ( ( str [ i ] , i ) )
        while len ( arr ) >= 3 and arr [ - 3 ] [ 0 ] == '1' and arr [ - 2 ] [ 0 ] == '0' and arr [ - 1 ] [ 0 ] == '0' :
            arr.pop ( - 3 )
            arr.pop ( - 2 )
            arr.pop ( - 1 )
        tmp = arr [ - 1 ] [ 1 ]
        maxlen = max ( maxlen , i - tmp )
    return maxlen

if __name__ == '__main__':
    param = [
    ('U',),
    ('544',),
    ('111',),
    (' cDQaNxpRSOe',),
    ('42920062459',),
    ('00100101',),
    ('FiC',),
    ('302746335230',),
    ('1',),
    ('ZBLHiwGreUR ',)
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
