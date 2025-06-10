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
def f_gold ( s , t ) :
    count = 0
    for i in range ( 0 , len ( t ) ) :
        if ( count == len ( s ) ) :
            break
        if ( t [ i ] == s [ count ] ) :
            count = count + 1
    return count


def f_filled ( s , t ) :
    count = 0
    for c in t :
        if count == len ( t ) :
            break
        if c == s [ count ] :
            count += 1
    return count

if __name__ == '__main__':
    param = [
    ('nObYIOjEQZ','uARTDTQbmGI',),
    ('84574','8457429',),
    ('1010001010010','11',),
    ('DjZtAfUudk','OewGm',),
    ('550','132744553919',),
    ('1110','0101',),
    ('GywyxwH','LPQqEqrDZiwY',),
    ('67318370914755','9928',),
    ('11011000000101','00000',),
    ('G','V',)
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
