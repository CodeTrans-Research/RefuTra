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
def f_gold ( limit ) :
    if ( limit < 2 ) :
        return 0
    ef1 = 0
    ef2 = 2
    sm = ef1 + ef2
    while ( ef2 <= limit ) :
        ef3 = 4 * ef2 + ef1
        if ( ef3 > limit ) :
            break
        ef1 = ef2
        ef2 = ef3
        sm = sm + ef2
    return sm


def f_filled ( limit ) :
    if limit < 2 :
        return 0
    ef1 , ef2 = 0 , 2
    sum = ef1 + ef2
    while ef2 <= limit :
        ef3 = 4 * ef2 + ef1
        if ef3 > limit :
            break
        ef1 , ef2 = ef2 , ef3
        sum += ef2
    return int ( sum )

if __name__ == '__main__':
    param = [
    (67,),
    (89,),
    (12,),
    (94,),
    (96,),
    (25,),
    (49,),
    (8,),
    (33,),
    (59,)
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
