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
def f_gold ( x ) :
    next = 0
    if ( x ) :
        rightOne = x & - ( x )
        nextHigherOneBit = x + int ( rightOne )
        rightOnesPattern = x ^ int ( nextHigherOneBit )
        rightOnesPattern = ( int ( rightOnesPattern ) / int ( rightOne ) )
        rightOnesPattern = int ( rightOnesPattern ) >> 2
        next = nextHigherOneBit | rightOnesPattern
    return next


def f_filled(x):
    rightOne = 0
    nextHigherOneBit = 0
    rightOnesPattern = 0
    next = 0

    if x > 0:
        rightOne = x & -x
        nextHigherOneBit = x + rightOne
        rightOnesPattern = x ^ nextHigherOneBit
        rightOnesPattern = (rightOnesPattern) // rightOne
        rightOnesPattern >>= 2
        next = nextHigherOneBit | rightOnesPattern

    return next

if __name__ == '__main__':
    param = [
    (42,),
    (75,),
    (94,),
    (5,),
    (52,),
    (22,),
    (77,),
    (44,),
    (85,),
    (59,)
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
