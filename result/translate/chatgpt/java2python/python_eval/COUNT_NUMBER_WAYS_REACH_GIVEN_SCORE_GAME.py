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
def f_gold ( n ) :
    table = [ 0 for i in range ( n + 1 ) ]
    table [ 0 ] = 1
    for i in range ( 3 , n + 1 ) :
        table [ i ] += table [ i - 3 ]
    for i in range ( 5 , n + 1 ) :
        table [ i ] += table [ i - 5 ]
    for i in range ( 10 , n + 1 ) :
        table [ i ] += table [ i - 10 ]
    return table [ n ]


def f_filled(n):
    table = [0] * (n + 1)
    table[0] = 1
    
    for i in range(3, n + 1):
        table[i] += table[i - 3]
    
    for i in range(5, n + 1):
        table[i] += table [i - 5]
    
    for i in range(10, n + 1):
        table[i] += table[i - 10]
    
    return table[n]

if __name__ == '__main__':
    param = [
    (83,),
    (29,),
    (17,),
    (12,),
    (93,),
    (55,),
    (97,),
    (75,),
    (22,),
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
            if set([filledres,goldres]) == set([float("inf"),sys.maxsize]) or set([filledres,goldres]) <= set([float("-inf"),-sys.maxsize-1,-sys.maxsize]):
                n_success += 1
    print("#Results: %i, %i" % (n_success, len(param)))
