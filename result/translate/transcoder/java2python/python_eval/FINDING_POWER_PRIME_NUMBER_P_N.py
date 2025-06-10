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
def f_gold ( n , p ) :
    ans = 0 ;
    temp = p ;
    while ( temp <= n ) :
        ans += int(n / temp) ;
        temp = temp * p ;
    return ans ;


def f_filled ( n , p ) :
    ans = 0
    for i in range ( 1 , n + 1 ) :
        count , temp = 0 , i
        while temp % p == 0 :
            count += 1
            temp = temp // p
        ans += count
    return ans

if __name__ == '__main__':
    param = [
    (49,30,),
    (80,25,),
    (10,9,),
    (81,57,),
    (11,4,),
    (45,34,),
    (86,90,),
    (27,78,),
    (80,60,),
    (97,31,)
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
