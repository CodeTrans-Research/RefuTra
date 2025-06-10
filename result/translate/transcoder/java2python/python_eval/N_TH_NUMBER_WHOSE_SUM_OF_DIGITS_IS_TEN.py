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
import itertools

def f_gold ( n ) :
    count = 0
    for curr in itertools.count ( ) :
        sum = 0
        x = curr
        while ( x ) :
            sum = sum + x % 10
            x = x // 10
        if ( sum == 10 ) :
            count = count + 1
        if ( count == n ) :
            return curr
    return - 1


def f_filled ( n ) :
    count = 0
    for curr in range ( 1 , 1 ) :
        sum = 0
        for x in range ( curr , 0 , 10 ) :
            sum = sum + x % 10
        if sum == 10 :
            count += 1
        if count == n :
            return curr

if __name__ == '__main__':
    param = [
    (37,),
    (13,),
    (51,),
    (69,),
    (76,),
    (10,),
    (97,),
    (40,),
    (69,),
    (4,)
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
