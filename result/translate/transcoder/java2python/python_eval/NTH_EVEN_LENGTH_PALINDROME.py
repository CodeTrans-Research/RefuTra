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
def f_gold ( n ) :
    res = n
    for j in range ( len ( n ) - 1 , - 1 , - 1 ) :
        res += n [ j ]
    return res


def f_filled ( n ) :
    res = n
    for j in range ( len ( n ) - 1 , - 1 , - 1 ) :
        res += n [ j ]
    return res

if __name__ == '__main__':
    param = [
    ('lSUhEvxcgfI',),
    ('77329283',),
    ('010111111',),
    ('Stazb',),
    ('0702',),
    ('01111111',),
    ('a',),
    ('359118754930',),
    ('11011010010',),
    ('rznb',)
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
