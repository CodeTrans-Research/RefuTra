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
    i = 0
    ans = 0
    while ( ( 1 << i ) <= n ) :
        k = 0
        change = 1 << i
        for j in range ( 0 , n + 1 ) :
            ans += k
            if change == 1 :
                k = not k
                change = 1 << i
            else :
                change -= 1
        i += 1
    return ans


def f_filled ( n ) :
    i = 0
    ans = 0
    while ( 1 << i ) <= n :
        k = False
        change = 1 << i
        j=0 
        while j<n+1 :
            if k == True :
                ans += 1
            else :
                ans += 0
            if change == 1 :
                k = not k
                change = 1 << i
            else :
                change -= 1
            j += 1
        i += 1
    return ans

if __name__ == '__main__':
    param = [
    (90,),
    (56,),
    (43,),
    (31,),
    (77,),
    (35,),
    (43,),
    (66,),
    (15,),
    (95,)
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
