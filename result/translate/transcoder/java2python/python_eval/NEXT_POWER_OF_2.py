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
def f_gold ( n ) :
    count = 0 ;
    if ( n and not ( n & ( n - 1 ) ) ) :
        return n
    while ( n != 0 ) :
        n >>= 1
        count += 1
    return 1 << count ;


def f_filled ( n ) :
    count = 0
    if n and ( n & ( n - 1 ) ) == 0 :
        return n
    while n != 0 :
        n >>= 1
        count += 1
    return 1 << count

if __name__ == '__main__':
    param = [
    (74,),
    (70,),
    (85,),
    (78,),
    (71,),
    (32,),
    (97,),
    (90,),
    (64,),
    (48,)
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
