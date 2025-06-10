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

def f_gold ( n ) :
    result = 0
    for i in range ( 2 , int (math.sqrt ( n )) + 1 ) :
        if ( n % i == 0 ) :
            if ( i == ( n / i ) ) :
                result = result + i
            else :
                result = result + ( i + n // i )
    return ( result + n + 1 )


def f_filled ( n ) :
    result = 0
    i=2 
    while i<=math.sqrt(n) :
        if n % i == 0 :
            if i == ( n / i ) :
                result += i
            else :
                result += ( i + n / i )
        i += 1
    return ( result + n + 1 )

if __name__ == '__main__':
    param = [
    (76,),
    (21,),
    (4,),
    (49,),
    (35,),
    (55,),
    (43,),
    (39,),
    (36,),
    (5,)
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
