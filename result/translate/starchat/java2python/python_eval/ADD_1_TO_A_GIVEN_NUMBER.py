import sys
import math
import heapq
from queue import Queue# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( x ) :
    m = 1 ;
    while ( x & m ) :
        x = x ^ m
        m <<= 1
    x = x ^ m
    return x


def f_filled(x):
        m = 1
        while (x & m) >= 1:
            x = x ^ m
            m = m << 1
        return x

if __name__ == '__main__':
    param = [
    (96,),
    (66,),
    (67,),
    (13,),
    (75,),
    (78,),
    (1,),
    (83,),
    (27,),
    (65,)
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

