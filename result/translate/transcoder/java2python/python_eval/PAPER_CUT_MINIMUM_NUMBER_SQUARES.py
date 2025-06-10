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
def f_gold ( a , b ) :
    result = 0
    rem = 0
    if ( a < b ) :
        a , b = b , a
    while ( b > 0 ) :
        result += int ( a / b )
        rem = int ( a % b )
        a = b
        b = rem
    return result


def f_filled ( a , b ) :
    result , rem = 0 , 0
    if a < b :
        swap ( a , b )
    while b :
        result += a // b
        rem = a % b
        a , b = b , rem
    return result

if __name__ == '__main__':
    param = [
    (87,60,),
    (18,35,),
    (68,93,),
    (80,20,),
    (87,69,),
    (64,29,),
    (64,1,),
    (65,95,),
    (43,72,),
    (97,41,)
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
