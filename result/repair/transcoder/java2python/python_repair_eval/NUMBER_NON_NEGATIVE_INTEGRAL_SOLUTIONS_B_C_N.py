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
    result = 0
    for i in range ( n + 1 ) :
        for j in range ( n + 1 ) :
            for k in range ( n + 1 ) :
                if i + j + k == n :
                    result += 1
    return result


def f_filled ( n ) :
    result = 0
    i=0 
    while i<n+1 :
        j=0 
        while j<n-i+1 :
            k=0 
            while k<(n-i-j)+1 :
                if i + j + k == n :
                    result += 1
                k += 1
            j += 1
        i += 1
    return result

if __name__ == '__main__':
    param = [
    (62,),
    (44,),
    (37,),
    (81,),
    (14,),
    (20,),
    (76,),
    (72,),
    (96,),
    (52,)
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
