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
    if ( n == 0 or n == 1 ) :
        return n
    return max ( ( f_gold ( n // 2 ) + f_gold ( n // 3 ) + f_gold ( n // 4 ) ) , n )


def f_filled ( n ) :
    if n == 0 or n == 1 :
        return n
    return max ( ( f_filled ( n / 2 ) + f_filled ( n / 3 ) + f_filled ( n / 4 ) ) , n )

if __name__ == '__main__':
    param = [
    (39,),
    (79,),
    (7,),
    (76,),
    (48,),
    (18,),
    (58,),
    (17,),
    (36,),
    (5,)
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
