import sys
import math
import heapq
from queue import Queue# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( a , b ) :
    if a == 0 :
        return b
    return f_gold ( b % a , a )


def f_filled(a: int, b: int) -> int:
        if a == 0:
            return b
        return f_filled(b % a, a)

if __name__ == '__main__':
    param = [
    (46,89,),
    (26,82,),
    (40,12,),
    (58,4,),
    (25,44,),
    (2,87,),
    (8,65,),
    (21,87,),
    (82,10,),
    (17,61,)
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
