import sys
import math
import heapq
from queue import Queue# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
from math import floor

def f_gold ( a , b ) :
    return floor ( ( a + b ) / 2 )


def f_filled(a, b):
        return (a + b) // 2

if __name__ == '__main__':
    param = [
    (1,44,),
    (6,61,),
    (75,20,),
    (51,17,),
    (19,25,),
    (82,98,),
    (72,21,),
    (48,41,),
    (12,17,),
    (41,80,)
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
