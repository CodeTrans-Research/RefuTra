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
    if ( n == 0 ) :
        return "0" ;
    bin = "" ;
    while ( n > 0 ) :
        if ( n & 1 == 0 ) :
            bin = '0' + bin ;
        else :
            bin = '1' + bin ;
        n = n >> 1 ;
    return bin ;


def f_filled ( n ) :
    if n == 0 :
        return '0'
    bin = ''
    while n :
        bin = ( ( n & 1 ) == 0 and '0' or '1' ) + bin
        n >>= 1
    return bin

if __name__ == '__main__':
    param = [
    (35,),
    (17,),
    (8,),
    (99,),
    (57,),
    (39,),
    (99,),
    (14,),
    (22,),
    (7,)
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
