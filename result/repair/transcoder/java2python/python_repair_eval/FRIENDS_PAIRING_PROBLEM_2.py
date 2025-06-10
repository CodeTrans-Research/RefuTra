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
    a , b , c = 1 , 2 , 0 ;
    if ( n <= 2 ) :
        return n ;
    for i in range ( 3 , n + 1 ) :
        c = b + ( i - 1 ) * a ;
        a = b ;
        b = c ;
    return c ;


def f_filled ( n ) :
    a , b , c = 1 , 2 , 0
    if n <= 2 :
        return n
    i=3 
    while i<n+1 :
        c = b + ( i - 1 ) * a
        a , b , c = b , c , c
        i += 1
    return c

if __name__ == '__main__':
    param = [
    (24,),
    (1,),
    (91,),
    (90,),
    (89,),
    (29,),
    (3,),
    (60,),
    (75,),
    (14,)
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
