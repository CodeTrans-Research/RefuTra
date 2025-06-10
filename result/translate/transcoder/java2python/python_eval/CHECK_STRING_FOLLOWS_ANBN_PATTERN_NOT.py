import sys
import math
import heapq
from queue import Queue
import numpy as np
# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( str ) :
    n = len ( str )
    for i in range ( n ) :
        if ( str [ i ] != 'a' ) :
            break
    if ( i * 2 != n ) :
        return False
    for j in range ( i , n ) :
        if ( str [ j ] != 'b' ) :
            return False
    return True


def f_filled ( s ) :
    l = len ( s )
    if l % 2 == 1 :
        return False
    i = 0
    j = l - 1
    while i < j :
        if s [ i ] != 'a' or s [ j ] != 'b' :
            return False
        i += 1
        j -= 1
    return True

if __name__ == '__main__':
    param = [
    ('ba',),
    ('aabb',),
    ('abab',),
    ('aaabb',),
    ('aabbb',),
    ('abaabbaa',),
    ('abaababb',),
    ('bbaa',),
    ('11001000',),
    ('ZWXv te',)
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
