import sys
import math
import heapq
from queue import Queue
# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
import math

def f_gold ( n ) :
    ans = 0
    for length in range ( 1 , int ( math.sqrt ( n ) ) + 1 ) :
        height = length
        while ( height * length <= n ) :
            ans += 1
            height += 1
    return ans


def f_filled(n):
    ans = 0
    for length in range(1, int(n**0.5)+1):
        for height in range(length, n//length+1):
            ans += 1
    return ans

if __name__ == '__main__':
    param = [
    (34,),
    (49,),
    (41,),
    (17,),
    (67,),
    (38,),
    (59,),
    (64,),
    (61,),
    (58,)
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
            if set([filledres,goldres]) == set([float("inf"),sys.maxsize]) or set([filledres,goldres]) <= set([float("-inf"),-sys.maxsize-1,-sys.maxsize]):
                n_success += 1
    print("#Results: %i, %i" % (n_success, len(param)))
