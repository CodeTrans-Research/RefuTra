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
def f_gold ( arr , l , r , x ) :
    if r < l :
        return - 1
    if arr [ l ] == x :
        return l
    if arr [ r ] == x :
        return r
    return f_gold ( arr , l + 1 , r - 1 , x )


def f_filled ( arr , l , r , x ) :
    if r < l :
        return - 1
    if arr [ l ] == x :
        return l
    if arr [ r ] == x :
        return r
    return f_filled ( arr , l + 1 , r - 1 , x )

if __name__ == '__main__':
    param = [
    ([10,74,5],0,2,1,),
    ([-90,72,36,96,42,0,-66,5],0,7,96,),
    ([0,5],0,1,-1,),
    ([99,70,67,5],0,3,3,),
    ([-98,-98,-26,-26,-24,-18,-16,80,5],0,8,80,),
    ([1,1,1,1,0,1,5],0,6,1,),
    ([1,5,12,12,17,17,12,95,96,98,5],0,0,12,),
    ([50,-70,-30,-54,6,-10,70,84,5],0,8,27,),
    ([0,1,5],0,2,14,),
    ([59,21,28,3,14,5],0,5,28,)
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

