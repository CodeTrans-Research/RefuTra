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
    maxPrime = - 1
    while n % 2 == 0 :
        maxPrime = 2
        n >>= 1
    for i in range ( 3 , int ( math.sqrt ( n ) ) + 1 , 2 ) :
        while n % i == 0 :
            maxPrime = i
            n = n / i
    if n > 2 :
        maxPrime = n
    return int ( maxPrime )


def f_filled ( n ) :
    max_prime = - 1
    while n % 2 == 0 :
        max_prime = 2
        n >>= 1
    for i in range ( 3 , math.sqrt ( n ) , 2 ) :
        while n % i == 0 :
            max_prime = i
            n = n / i
    if n > 2 :
        max_prime = n
    return max_prime

if __name__ == '__main__':
    param = [
    (98,),
    (8,),
    (78,),
    (65,),
    (55,),
    (10,),
    (10,),
    (37,),
    (39,),
    (15,)
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
