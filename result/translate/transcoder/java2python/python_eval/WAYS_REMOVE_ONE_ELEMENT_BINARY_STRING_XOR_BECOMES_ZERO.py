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
    one_count = 0
    zero_count = 0
    n = len ( str )
    for i in range ( 0 , n , 1 ) :
        if ( str [ i ] == '1' ) :
            one_count += 1
        else :
            zero_count += 1
    if ( one_count % 2 == 0 ) :
        return zero_count
    return one_count


def f_filled ( s ) :
    one_count , zero_count = 0 , 0
    str = s.split ( )
    n = len ( str )
    for i in range ( n ) :
        if str [ i ] == '1' :
            one_count += 1
        else :
            zero_count += 1
    if one_count % 2 == 0 :
        return zero_count
    return one_count

if __name__ == '__main__':
    param = [
    ('KfcTJNP',),
    ('05312505872',),
    ('100111',),
    ('tDEEhKxrQ',),
    ('50824233019',),
    ('10001110010',),
    ('T SEZaNm MYQ',),
    ('838415739',),
    ('01110100',),
    ('WYQiAey H',)
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
