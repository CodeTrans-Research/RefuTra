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
    count = 0
    while ( n ) :
        n &= ( n - 1 )
        count += 1
    return count


def f_filled(n):
    count = 0
    while n > 0:
        n &= (n - 1)
        count += 1
    return count

if __name__ == '__main__':
    param = [
    (32,),
    (94,),
    (33,),
    (99,),
    (17,),
    (64,),
    (80,),
    (42,),
    (12,),
    (86,)
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
