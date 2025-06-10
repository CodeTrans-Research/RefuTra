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
    odd_count = 0
    even_count = 0
    if ( n < 0 ) :
        n = - n
    if ( n == 0 ) :
        return 1
    if ( n == 1 ) :
        return 0
    while ( n ) :
        if ( n & 1 ) :
            odd_count += 1
        if ( n & 2 ) :
            even_count += 1
        n = n >> 2
    return f_gold ( abs ( odd_count - even_count ) )


def f_filled(n):
    odd_count = 0
    even_count = 0
    if n < 0:
        n = -n
    if n == 0:
        return 1
    if n == 1:
        return 0
    while n != 0:
        if (n & 1) != 0:
            odd_count += 1
        if (n & 2) != 0:
            even_count += 1
        n = n >> 2
    return f_filled(abs(odd_count - even_count))

if __name__ == '__main__':
    param = [
    (94,),
    (94,),
    (79,),
    (39,),
    (16,),
    (90,),
    (64,),
    (76,),
    (83,),
    (47,)
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
