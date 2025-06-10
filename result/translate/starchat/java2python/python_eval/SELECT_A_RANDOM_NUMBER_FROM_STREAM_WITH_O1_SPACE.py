import sys
import math
import heapq
from queue import Queue# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
import random
def f_gold ( x ) :
    res = 0 ;
    count = 0 ;
    count += 1 ;
    if ( count == 1 ) :
        res = x ;
    else :
        i = random.randrange ( count ) ;
        if ( i == count - 1 ) :
            res = x ;
    return res ;


def f_filled(x):
        res = 0
        count = 0
        count += 1
        if count == 1:
            res = x
        else:
            import random
            i = random.randint(0, count - 1)
            if i == count - 1:
                res = x
        return res

if __name__ == '__main__':
    param = [
    (64,),
    (36,),
    (21,),
    (3,),
    (18,),
    (82,),
    (76,),
    (99,),
    (70,),
    (31,)
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

