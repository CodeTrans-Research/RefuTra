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
    a = [ 0 ] * n
    b = [ 0 ] * n
    a [ 0 ] = b [ 0 ] = 1
    for i in range ( 1 , n ) :
        a [ i ] = a [ i - 1 ] + b [ i - 1 ]
        b [ i ] = a [ i - 1 ]
    return ( 1 << n ) - a [ n - 1 ] - b [ n - 1 ]


def f_filled(n):
    a = [0] * n
    b = [0] * n
    a[0] = b[0] = 1
    for i in range(1, n):
        a[i] = a[i - 1] + b[i - 1]
        b[i] = a[i - 1]
    
    return (1 << n) - a[n - 1] - b[n - 1]

if __name__ == '__main__':
    param = [
    (27,),
    (72,),
    (13,),
    (83,),
    (75,),
    (33,),
    (57,),
    (51,),
    (10,),
    (1,)
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
