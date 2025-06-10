import sys
import math
import heapq
from queue import Queue# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( x , y ) :
    if ( y == 0 ) :
        return 0
    if ( y > 0 ) :
        return ( x + f_gold ( x , y - 1 ) )
    if ( y < 0 ) :
        return - f_gold ( x , - y )


def f_filled(x, y):
        if y == 0:
            return 0
        if y > 0:
            return (x + f_filled(x, y - 1))
        if y < 0:
            return -f_filled(x, -y)
        return -1

if __name__ == '__main__':
    param = [
    (18,94,),
    (23,36,),
    (24,22,),
    (75,92,),
    (25,43,),
    (57,32,),
    (31,57,),
    (8,17,),
    (12,76,),
    (74,70,)
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
