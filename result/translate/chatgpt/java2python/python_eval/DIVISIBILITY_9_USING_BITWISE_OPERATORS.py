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
def f_gold ( n ) :
    if ( n == 0 or n == 9 ) :
        return True
    if ( n < 9 ) :
        return False
    return f_gold ( ( int ) ( n >> 3 ) - ( int ) ( n & 7 ) )


def f_filled(n):
    if n == 0 or n == 9:
        return True
    if n < 9:
        return False
    return f_filled((n >> 3) - (n & 7))

if __name__ == '__main__':
    param = [
    (96,),
    (85,),
    (54,),
    (14,),
    (47,),
    (11,),
    (49,),
    (99,),
    (28,),
    (82,)
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
