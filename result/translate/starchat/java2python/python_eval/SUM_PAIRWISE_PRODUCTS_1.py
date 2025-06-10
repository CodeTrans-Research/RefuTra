import sys
import math
import heapq
from queue import Queue# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( n ) :
    multiTerms = n * ( n + 1 ) // 2
    sm = multiTerms
    for i in range ( 2 , n + 1 ) :
        multiTerms = multiTerms - ( i - 1 )
        sm = sm + multiTerms * i
    return sm


def f_filled(n):
        multiTerms = n * (n + 1) // 2
        sum = multiTerms
        for i in range(2, n + 1):
            multiTerms = multiTerms - (i - 1)
            sum = sum + multiTerms * i
        return sum

if __name__ == '__main__':
    param = [
    (41,),
    (50,),
    (67,),
    (18,),
    (60,),
    (6,),
    (27,),
    (46,),
    (50,),
    (20,)
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
