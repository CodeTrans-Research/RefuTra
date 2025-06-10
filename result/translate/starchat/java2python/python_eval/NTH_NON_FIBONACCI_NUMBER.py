import sys
import math
import heapq
from queue import Queue# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( n ) :
    prevPrev = 1
    prev = 2
    curr = 3
    while n > 0 :
        prevPrev = prev
        prev = curr
        curr = prevPrev + prev
        n = n - ( curr - prev - 1 )
    n = n + ( curr - prev - 1 )
    return prev + n


def f_filled(n):
        prevPrev, prev, curr = 1, 2, 3
        while n > 0:
            prevPrev, prev, curr = prev, curr, prevPrev + prev
            n -= (curr - prev - 1)
        return prev + n

if __name__ == '__main__':
    param = [
    (76,),
    (91,),
    (62,),
    (65,),
    (83,),
    (57,),
    (76,),
    (6,),
    (2,),
    (86,)
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
