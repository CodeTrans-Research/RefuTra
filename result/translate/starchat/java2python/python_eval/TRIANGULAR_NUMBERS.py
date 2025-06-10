import sys
import math
import heapq
from queue import Queue# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( num ) :
    if ( num < 0 ) :
        return False
    sum , n = 0 , 1
    while ( sum <= num ) :
        sum = sum + n
        if ( sum == num ) :
            return True
        n += 1
    return False


def f_filled(num):
        if num < 0:
            return False
        sum = 0
        for n in range(1, num + 1):
            sum += n
            if sum == num:
                return True
        return False

if __name__ == '__main__':
    param = [
    (97,),
    (97,),
    (32,),
    (40,),
    (18,),
    (14,),
    (90,),
    (39,),
    (1,),
    (57,)
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
