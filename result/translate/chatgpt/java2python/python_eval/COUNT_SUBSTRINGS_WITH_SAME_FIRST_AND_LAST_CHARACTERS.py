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
def f_gold ( s ) :
    result = 0 ;
    n = len ( s ) ;
    for i in range ( n ) :
        for j in range ( i , n ) :
            if ( s [ i ] == s [ j ] ) :
                result = result + 1
    return result


def f_filled(s):
    result = 0
    n = len(s)
    for i in range(n):
        for j in range(i, n):
            if s[i] == s[j]:
                result += 1
    return result

if __name__ == '__main__':
    param = [
    ('LZIKA',),
    ('0556979952',),
    ('110010',),
    ('kGaYfd',),
    ('413567670657',),
    ('01001',),
    ('EQPuFa',),
    ('48848378',),
    ('110',),
    ('PLehNeP',)
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
