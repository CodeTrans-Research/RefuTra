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
import math

def f_gold ( a , b ) :
    if ( a == 0 or b == 0 ) :
        return 1
    return math.floor ( math.log10 ( abs ( a ) ) + math.log10 ( abs ( b ) ) ) + 1


def f_filled ( a , b ) :
    if a == 0 or b == 0 :
        return 1
    return int ( math.floor ( math.log10 ( abs ( a ) ) + math.log10 ( abs ( b ) ) ) ) + 1

if __name__ == '__main__':
    param = [
    (97,91,),
    (52,49,),
    (95,34,),
    (35,40,),
    (40,85,),
    (18,97,),
    (92,15,),
    (73,98,),
    (10,62,),
    (82,22,)
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
