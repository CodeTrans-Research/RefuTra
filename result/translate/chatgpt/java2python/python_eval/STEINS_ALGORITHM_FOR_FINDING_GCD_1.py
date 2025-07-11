import sys
import math
import heapq
from queue import Queue
# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( a , b ) :
    if ( a == b ) :
        return a
    if ( a == 0 ) :
        return b
    if ( b == 0 ) :
        return a
    if ( ( ~ a & 1 ) == 1 ) :
        if ( ( b & 1 ) == 1 ) :
            return f_gold ( a >> 1 , b )
        else :
            return ( f_gold ( a >> 1 , b >> 1 ) << 1 )
    if ( ( ~ b & 1 ) == 1 ) :
        return f_gold ( a , b >> 1 )
    if ( a > b ) :
        return f_gold ( ( a - b ) >> 1 , b )
    return f_gold ( ( b - a ) >> 1 , a )


def f_filled(a, b):
    if a == b:
        return a
    if a == 0:
        return b
    if b == 0:
        return a
    if (~a & 1) == 1:
        if b & 1 == 1:
            return f_filled(a >> 1, b)
        else:
            return f_filled(a >> 1, b >> 1) << 1
    if (~b & 1) == 1:
        return f_filled(a, b >> 1)
    if a > b:
        return f_filled((a - b) >> 1, b)
    return f_filled((b - a) >> 1, a)

if __name__ == '__main__':
    param = [
    (52,29,),
    (36,94,),
    (12,6,),
    (69,7,),
    (45,11,),
    (7,51,),
    (45,55,),
    (62,86,),
    (96,63,),
    (89,12,)
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
            if set([filledres,goldres]) == set([float("inf"),sys.maxsize]) or set([filledres,goldres]) <= set([float("-inf"),-sys.maxsize-1,-sys.maxsize]):
                n_success += 1
    print("#Results: %i, %i" % (n_success, len(param)))
