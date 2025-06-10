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
def f_gold ( x , y ) :
    return ( ( x ^ y ) < 0 ) ;


def f_filled ( x , y ) :
    return ( ( x ^ y ) < 0 )

if __name__ == '__main__':
    param = [
    (59,-99,),
    (-20,-21,),
    (-100,79,),
    (54,-49,),
    (-16,16,),
    (-23,-68,),
    (93,37,),
    (24,-61,),
    (-8,69,),
    (29,10,)
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
