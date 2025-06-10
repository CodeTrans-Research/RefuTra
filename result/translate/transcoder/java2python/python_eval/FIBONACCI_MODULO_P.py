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
def f_gold ( p ) :
    first = 1
    second = 1
    number = 2
    next = 1
    while ( next ) :
        next = ( first + second ) % p
        first = second
        second = next
        number = number + 1
    return number


def f_filled ( p ) :
    first , second , number , next = 1 , 1 , 2 , 1
    while next > 0 :
        next = ( first + second ) % p
        first , second = second , next
        number += 1
    return number

if __name__ == '__main__':
    param = [
    (51,),
    (40,),
    (68,),
    (7,),
    (8,),
    (32,),
    (93,),
    (75,),
    (71,),
    (15,)
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
