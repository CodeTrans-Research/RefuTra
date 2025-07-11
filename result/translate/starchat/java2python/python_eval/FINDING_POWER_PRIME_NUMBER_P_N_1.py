import sys
import math
import heapq
from queue import Queue# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( n , p ) :
    ans = 0
    temp = p
    while ( temp <= n ) :
        ans += n // temp
        temp = temp * p
    return ans 


def f_filled(n, p):
        ans = 0
        temp = p
        while temp <= n:
            ans += n // temp
            temp *= p
        return ans

if __name__ == '__main__':
    param = [
    (76,43,),
    (77,91,),
    (9,42,),
    (59,67,),
    (8,52,),
    (97,8,),
    (78,24,),
    (41,88,),
    (72,61,),
    (71,28,)
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
