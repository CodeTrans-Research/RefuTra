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
def f_gold ( str ) :
    n = len ( str )
    count = 0
    res = str [ 0 ]
    cur_count = 1
    for i in range ( n ) :
        if ( i < n - 1 and str [ i ] == str [ i + 1 ] ) :
            cur_count += 1
        else :
            if cur_count > count :
                count = cur_count
                res = str [ i ]
            cur_count = 1
    return res


def f_filled(str):
    n = len(str)
    count = 0
    res = str[0]
    cur_count = 1
    
    for i in range(n):
        if i < n - 1 and str[i] == str[i + 1]:
            cur_count += 1
        else:
            if cur_count > count:
                count = cur_count
                res = str[i]
            cur_count = 1
    
    return res

if __name__ == '__main__':
    param = [
    ('geeekk',),
    ('3786868',),
    ('110',),
    ('aaaabbcbbb',),
    ('11',),
    ('011101',),
    ('WoHNyJYLC',),
    ('3141711779',),
    ('10111101101',),
    ('aabbabababcc',)
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
