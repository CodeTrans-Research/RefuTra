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
def f_gold ( process , need ) :
    minResources = 0
    minResources = process * ( need - 1 ) + 1
    return minResources


def f_filled ( process , need ) :
    min_resources = 0
    min_resources = process * ( need - 1 ) + 1
    return min_resources

if __name__ == '__main__':
    param = [
    (38,37,),
    (82,3,),
    (2,26,),
    (38,72,),
    (31,85,),
    (80,73,),
    (11,9,),
    (2,31,),
    (26,59,),
    (37,67,)
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
