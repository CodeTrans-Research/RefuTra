import sys
import math
import heapq
from queue import Queue# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( n , x ) :
    cnt = 0
    for i in range ( 1 , n + 1 ) :
        if i <= x :
            if x // i <= n and x % i == 0 :
                cnt += 1
    return cnt


def f_filled(n, x):
        f_filled = 0
        for i in range(1, min(n, x) + 1):
            if x // i <= n and x % i == 0:
                f_filled += 1
        return f_filled

if __name__ == '__main__':
    param = [
    (47,0,),
    (57,16,),
    (55,63,),
    (11,23,),
    (55,49,),
    (63,64,),
    (64,98,),
    (28,30,),
    (49,61,),
    (48,64,)
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
