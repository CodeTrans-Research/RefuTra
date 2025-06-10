import sys
import math
import heapq
from queue import Queue# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( A , B ) :
    variable = 1
    if ( A == B ) :
        return 1
    elif ( ( B - A ) >= 5 ) :
        return 0
    else :
        for i in range ( A + 1 , B + 1 ) :
            variable = ( variable * ( i % 10 ) ) % 10
        return variable % 10


def f_filled(A, B):
        if A == B:
            return 1
        if (B - A) >= 5:
            return 0
        variable = 1
        for i in range(A + 1, B + 1):
            variable = (variable * (i % 10)) % 10
        return variable % 10

if __name__ == '__main__':
    param = [
    (79,84,),
    (61,29,),
    (39,77,),
    (39,65,),
    (61,78,),
    (86,73,),
    (7,92,),
    (86,50,),
    (86,63,),
    (11,2,)
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
