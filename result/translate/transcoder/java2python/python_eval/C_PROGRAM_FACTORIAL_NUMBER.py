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
    return 1 if ( n == 1 or n == 0 ) else n * f_gold ( n - 1 ) ;


def f_filled ( n ) :
    if n == 0 :
        return 1
    return n * f_filled ( n - 1 )

if __name__ == '__main__':
    param = [
    (84,),
    (41,),
    (5,),
    (38,),
    (79,),
    (80,),
    (64,),
    (62,),
    (24,),
    (12,)
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
