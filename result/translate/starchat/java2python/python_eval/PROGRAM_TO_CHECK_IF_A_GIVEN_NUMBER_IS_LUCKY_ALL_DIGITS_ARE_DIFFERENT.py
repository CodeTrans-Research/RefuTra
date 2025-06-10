import sys
import math
import heapq
from queue import Queue# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
import math

def f_gold ( n ) :
    ar = [ 0 ] * 10
    while ( n > 0 ) :
        digit = math.floor ( n % 10 )
        if ( ar [ digit ] ) :
            return False
        ar [ digit ] = 1
        n = int ( n / 10 )
    return True


def f_filled(n):
        arr = [False] * 10
        while n > 0:
            digit = n % 10
            if arr[digit]:
                return False
            arr[digit] = True
            n = n // 10
        return True

if __name__ == '__main__':
    param = [
    (474,),
    (9445,),
    (90,),
    (30,),
    (37453,),
    (27,),
    (2400,),
    (98,),
    (46,),
    (722,)
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

