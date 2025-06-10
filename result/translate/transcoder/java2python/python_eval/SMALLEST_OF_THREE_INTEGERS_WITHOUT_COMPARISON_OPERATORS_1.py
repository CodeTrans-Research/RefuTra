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
def f_gold ( x , y , z ) :
    if ( not int ( y / x )  ) :
        return y if ( not int ( y / z ) ) else z
    return x if ( not int ( x / z )  ) else z


def f_filled ( x , y , z ) :
    if ( y / x ) == 0 :
        return ( ( y / z ) == 0 )
    return ( ( x / z ) == 0 )

if __name__ == '__main__':
    param = [
    (48,63,56,),
    (11,55,84,),
    (50,89,96,),
    (21,71,74,),
    (94,39,42,),
    (22,44,86,),
    (3,41,68,),
    (67,62,94,),
    (59,2,83,),
    (50,11,1,)
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

