import sys
import math
import heapq
from queue import Queue# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( s ) :
    _sum = 0
    n = 1
    while ( _sum < s ) :
        _sum += n * n * n
        n += 1
    n -= 1
    if _sum == s :
        return n
    return - 1


def f_filled(s):
        sum = 0
        for n in range(1, s + 1):
            sum += n * n * n
            if sum == s:
                return n
        return -1

if __name__ == '__main__':
    param = [
    (15,),
    (36,),
    (39,),
    (43,),
    (75,),
    (49,),
    (56,),
    (14,),
    (62,),
    (97,)
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
