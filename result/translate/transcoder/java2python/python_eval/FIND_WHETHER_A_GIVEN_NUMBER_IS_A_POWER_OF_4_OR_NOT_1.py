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
    count = 0
    if ( n and ( not ( n & ( n - 1 ) ) ) ) :
        while ( n > 1 ) :
            n >>= 1
            count += 1
        if ( count % 2 == 0 ) :
            return True
        else :
            return False
    return False


def f_filled ( n ) :
    count = 0
    x = n & ( n - 1 )
    if n and x == 0 :
        while n > 1 :
            n >>= 1
            count += 1
        return ( count % 2 == 0 ) and True or False
    return False

if __name__ == '__main__':
    param = [
    (1,),
    (4,),
    (64,),
    (-64,),
    (128,),
    (1024,),
    (45,),
    (33,),
    (66,),
    (74,)
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
