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
    return ( n != 0 and ( ( n & ( n - 1 ) ) == 0 ) and not ( n & 0xAAAAAAAA ) ) ;


def f_filled(n):
    return n != 0 and ((n & (n - 1)) == 0) and (n & 0xAAAAAAAA) == 0

if __name__ == '__main__':
    param = [
    (1,),
    (4,),
    (64,),
    (-64,),
    (128,),
    (1024,),
    (97,),
    (86,),
    (14,),
    (99,)
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
