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
import math

def f_gold ( x , y ) :
    res1 = int ( math.log ( y ) / math.log ( x ) )
    res2 = math.log ( y ) / math.log ( x )
    return 1 if ( res1 == res2 ) else 0


def f_filled ( x , y ) :
    res1 = int ( np.log ( y ) / np.log ( x ) )
    res2 = np.log ( y ) / np.log ( x )
    return ( res1 == res2 )

if __name__ == '__main__':
    param = [
    (57,1,),
    (3,9,),
    (10,101,),
    (10,10000,),
    (6,46656,),
    (2,2048,),
    (2,40,),
    (20,79,),
    (96,98,),
    (25,5,)
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
