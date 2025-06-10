import sys
import math
import heapq
from queue import Queue
# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( n , p ) :
    n = n % p
    for x in range ( 2 , p , 1 ) :
        if ( ( x * x ) % p == n ) :
            return True
    return False


def f_filled(n, p):
    n = n % p
    for x in range(2, p):
        if (x * x) % p == n:
            return True
    return False

if __name__ == '__main__':
    param = [
    (71,78,),
    (85,75,),
    (4,35,),
    (20,99,),
    (71,29,),
    (72,88,),
    (36,54,),
    (95,52,),
    (83,33,),
    (72,13,)
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
            if set([filledres,goldres]) == set([float("inf"),sys.maxsize]) or set([filledres,goldres]) <= set([float("-inf"),-sys.maxsize-1,-sys.maxsize]):
                n_success += 1
    print("#Results: %i, %i" % (n_success, len(param)))
