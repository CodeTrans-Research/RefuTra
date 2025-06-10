import sys
import math
import heapq
from queue import Queue# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( str_ ) :
    n = len ( str_ )
    arr = [ 0 ] * n
    concat = str_ + str_
    for i in range ( n ) :
        arr [ i ] = concat [ i : n + i ]
    arr.sort ( )
    return arr [ 0 ]


def f_filled(str):
        n = len(str)
        arr = [""] * n
        concat = str + str
        for i in range(n):
            arr[i] = concat[i:i+n]
        arr.sort()
        return arr[0]

if __name__ == '__main__':
    param = [
    ('onWEchl',),
    ('2',),
    ('100',),
    ('GHbCZA',),
    ('50568798206105',),
    ('001011110001',),
    ('lljpYhznnyu',),
    ('54499921759984',),
    ('11101',),
    ('qvypgCYEjsyjwZ',)
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
