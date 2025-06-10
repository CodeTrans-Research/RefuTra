import sys
import math
import heapq
from queue import Queue# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( str ) :
    for i in range ( 0 , len ( str ) ) :
        if ( str [ i ].istitle ( ) ) :
            return str [ i ]
    return 0


def f_filled(str):
        for i in range(len(str)):
            if str[i].isupper():
                return ord(str[i])
        return 0

if __name__ == '__main__':
    param = [
    ('pH',),
    ('96544000',),
    ('000010000',),
    ('ujqpx',),
    ('20684847994',),
    ('111',),
    ('rclkv',),
    ('45173693434',),
    ('11111011001101',),
    ('f',)
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
