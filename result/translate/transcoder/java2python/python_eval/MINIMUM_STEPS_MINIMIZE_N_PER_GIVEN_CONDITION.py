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
    table = [ 0 ] * ( n + 1 )
    for i in range ( n + 1 ) :
        table [ i ] = n - i
    for i in range ( n , 0 , - 1 ) :
        if ( not ( i % 2 ) ) :
            table [ i // 2 ] = min ( table [ i ] + 1 , table [ i // 2 ] )
        if ( not ( i % 3 ) ) :
            table [ i // 3 ] = min ( table [ i ] + 1 , table [ i // 3 ] )
    return table [ 1 ]


def f_filled ( n ) :
    table = [ n - i for i in range ( n + 1 ) ]
    for i in range ( n , - 1 , - 1 ) :
        if not ( i % 2 > 0 ) :
            table [ i / 2 ] = min ( table [ i ] + 1 , table [ i / 2 ] )
        if not ( i % 3 > 0 ) :
            table [ i / 3 ] = min ( table [ i ] + 1 , table [ i / 3 ] )
    return table [ 1 : ]

if __name__ == '__main__':
    param = [
    (59,),
    (7,),
    (90,),
    (78,),
    (49,),
    (15,),
    (45,),
    (56,),
    (7,),
    (70,)
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
