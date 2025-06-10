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
    res = 1
    while n % 2 == 0 :
        n = n // 2
    for i in range ( 3 , int ( math.sqrt ( n ) + 1 ) ) :
        count = 0
        curr_sum = 1
        curr_term = 1
        while n % i == 0 :
            count += 1
            n = n // i
            curr_term *= i
            curr_sum += curr_term
        res *= curr_sum
    if n >= 2 :
        res *= ( 1 + n )
    return res


def f_filled ( n ) :
    res = 1
    while n % 2 == 0 :
        n = n / 2
    for i in range( 3 ,int ( math.sqrt ( n ) )):
        count , curr_sum = 0 , 1
        curr_term = 1
        while n % i == 0 :
            count += 1
            n = n / i
            curr_term *= i
            curr_sum += curr_term
        res *= curr_sum
    if n >= 2 :
        res *= ( 1 + n )
    return res

if __name__ == '__main__':
    param = [
    (20,),
    (6,),
    (39,),
    (80,),
    (88,),
    (7,),
    (16,),
    (27,),
    (83,),
    (6,)
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
