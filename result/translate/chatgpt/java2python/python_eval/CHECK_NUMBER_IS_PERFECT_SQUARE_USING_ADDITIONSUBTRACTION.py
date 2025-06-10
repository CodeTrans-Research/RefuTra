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
    i = 1
    the_sum = 0
    while the_sum < n :
        the_sum += i
        if the_sum == n :
            return True
        i += 2
    return False


def f_filled(n):
    sum_value = 0
    i = 1
    while sum_value < n:
        sum_value += i
        if sum_value == n:
            return True
        i += 2
    return False

if __name__ == '__main__':
    param = [
    (1,),
    (4,),
    (9,),
    (25,),
    (36,),
    (3,),
    (121,),
    (14,),
    (17,),
    (80,)
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
