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
    return n * ( n + 1 ) * ( n + 2 ) * ( 3 * n + 1 ) // 24


def f_filled(n):
        return n * (n + 1) * (n + 2) * (3 * n + 1) // 24

if __name__ == '__main__':
    param = [
    (10**10,),
    (18,),
    (97,),
    (9,),
    (42,),
    (67,),
    (71,),
    (66,),
    (69,),
    (18,)
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
