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
    zeros = 0
    ones = 0
    for i in range ( 0 , len ( str ) ) :
        ch = str [ i ] ;
        if ( ch == '0' ) :
            zeros = zeros + 1
        else :
            ones = ones + 1
    return ( zeros == 1 or ones == 1 ) ;


def f_filled(str):
        zeros, ones = 0, 0
        for i in range(len(str)):
            ch = str[i]
            if ch == '0':
                zeros += 1
            else:
                ones += 1
        return zeros == 1 or ones == 1

if __name__ == '__main__':
    param = [
    ("00001",),
    ("0000",),
    ("11",),
    ("111110",),
    ("1",),
    ("111010111010",),
    ("hUInqJXNdbfP",),
    ("5191",),
    ("1110101101",),
    ('NupSrU xz',)
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
