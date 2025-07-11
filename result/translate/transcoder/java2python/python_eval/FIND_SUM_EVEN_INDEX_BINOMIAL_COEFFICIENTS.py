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
    C = [ [ 0 for x in range ( n + 1 ) ] for y in range ( n + 1 ) ]
    for i in range ( 0 , n + 1 ) :
        for j in range ( 0 , min ( i , n ) + 1 ) :
            if j == 0 or j == i :
                C [ i ] [ j ] = 1
            else :
                C [ i ] [ j ] = C [ i - 1 ] [ j - 1 ] + C [ i - 1 ] [ j ]
    sum = 0 ;
    for i in range ( 0 , n + 1 ) :
        if i % 2 == 0 :
            sum = sum + C [ n ] [ i ]
    return sum


def f_filled ( n ) :
    C = [ [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0 ] * n + [ 0

if __name__ == '__main__':
    param = [
    (18,),
    (54,),
    (67,),
    (17,),
    (47,),
    (99,),
    (26,),
    (93,),
    (57,),
    (98,)
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
