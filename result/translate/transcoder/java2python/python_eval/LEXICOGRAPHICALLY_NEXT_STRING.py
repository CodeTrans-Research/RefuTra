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
def f_gold ( s ) :
    if ( s == " " ) :
        return "a"
    i = len ( s ) - 1
    while ( s [ i ] == 'z' and i >= 0 ) :
        i -= 1
    if ( i == - 1 ) :
        s = s + 'a'
    else :
        s = s [ 0 : i ] + chr ( ord ( s [ i ] ) + 1 ) + s [ i + 1 : ]
    return s


def f_filled ( str ) :
    if str == "" :
        return "a"
    i = len ( str ) - 1
    while str [ i ] == "z" and i >= 0 :
        i -= 1
    if i == - 1 :
        str = str + 'a'
    else :
        str = str [ : i ] + chr ( ord ( str [ i ] ) + 1 ) + str [ i + 1 : ]
    return str

if __name__ == '__main__':
    param = [
    ('amKIRzPiqLTIy',),
    ('68',),
    ('100',),
    ('f',),
    ('802205375',),
    ('0111',),
    ('GRjRYIvYwgua',),
    ('8139910006809',),
    ('100101',),
    ('rw',)
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
