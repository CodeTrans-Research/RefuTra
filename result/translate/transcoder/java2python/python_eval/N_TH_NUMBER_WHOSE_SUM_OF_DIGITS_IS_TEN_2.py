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

def f_gold ( n ) :
    nthElement = 19 + ( n - 1 ) * 9
    outliersCount = int ( math.log10 ( nthElement ) ) - 1
    nthElement += 9 * outliersCount
    return nthElement


def f_filled ( n ) :
    nth_element = 19 + ( n - 1 ) * 9
    outliers_count = int ( math.log10 ( nth_element ) ) - 1
    nth_element += 9 * outliers_count
    return nth_element

if __name__ == '__main__':
    param = [
    (68,),
    (70,),
    (69,),
    (93,),
    (99,),
    (44,),
    (91,),
    (8,),
    (83,),
    (51,)
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
