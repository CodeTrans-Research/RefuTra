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
def f_gold ( n ) :
    der = [ 0 for i in range ( n + 1 ) ]
    der [ 0 ] = 1
    der [ 1 ] = 0
    der [ 2 ] = 1
    for i in range ( 3 , n + 1 ) :
        der [ i ] = ( i - 1 ) * ( der [ i - 1 ] + der [ i - 2 ] )
    return der [ n ]


def f_filled(n):
    der = [0] * (n + 1)
    der[0] = 1
    der[1] = 0
    der[2] = 1
    for i in range(3, n + 1):
        der[i] = (i - 1) * (der[i - 1] + der[i - 2])
    return der[n]

if __name__ == '__main__':
    param = [
    (22,),
    (91,),
    (33,),
    (93,),
    (90,),
    (59,),
    (88,),
    (41,),
    (70,),
    (63,)
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
