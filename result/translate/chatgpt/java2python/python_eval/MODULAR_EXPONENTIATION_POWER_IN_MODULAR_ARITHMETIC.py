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
def f_gold ( x , y , p ) :
    res = 1
    x = x % p
    while ( y > 0 ) :
        if ( ( y & 1 ) == 1 ) :
            res = ( res * x ) % p
        y = y >> 1
        x = ( x * x ) % p
    return res


def f_filled(x, y, p):
    res = 1
    x = x % p
    while y > 0:
        if y & 1 == 1:
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res

if __name__ == '__main__':
    param = [
    (45,5,68,),
    (67,25,49,),
    (26,91,44,),
    (33,61,9,),
    (35,8,13,),
    (68,41,5,),
    (14,76,20,),
    (5,89,13,),
    (23,42,45,),
    (37,63,56,)
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
