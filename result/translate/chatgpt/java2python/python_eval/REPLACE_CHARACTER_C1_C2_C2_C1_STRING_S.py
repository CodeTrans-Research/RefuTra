import sys
import math
import heapq
from queue import Queue
# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( s , c1 , c2 ) :
    l = len ( s )
    for i in range ( l ) :
        if ( s [ i ] == c1 ) :
            s = s [ 0 : i ] + c2 + s [ i + 1 : ]
        elif ( s [ i ] == c2 ) :
            s = s [ 0 : i ] + c1 + s [ i + 1 : ]
    return s


def f_filled(s, c1, c2):
    l = len(s)
    arr = list(s)
    for i in range(l):
        if arr[i] == c1:
            arr[i] = c2
        elif arr[i] == c2:
            arr[i] = c1
    return ''.join(arr)

if __name__ == '__main__':
    param = [
    ('IZTSMw j','W','k',),
    ('7288334','6','9',),
    ('010110000','1','1',),
    ('b gJX','t','P',),
    ('734','4','4',),
    ('1','1','1',),
    ('xCaUKdhA','X','S',),
    ('4370992644981','5','6',),
    ('01010','0','1',),
    ('ZNIFGshaWA','Q','x',)
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
            if set([filledres,goldres]) == set([float("inf"),sys.maxsize]) or set([filledres,goldres]) <= set([float("-inf"),-sys.maxsize-1,-sys.maxsize]):
                n_success += 1
    print("#Results: %i, %i" % (n_success, len(param)))
