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
def f_gold ( num ) :
    series = [ 1 , 3 , 2 , - 1 , - 3 , - 2 ] ;
    series_index = 0 ;
    result = 0 ;
    for i in range ( ( len ( num ) - 1 ) , - 1 , - 1 ) :
        digit = ord ( num [ i ] ) - 48 ;
        result += digit * series [ series_index ] ;
        series_index = ( series_index + 1 ) % 6 ;
        result %= 7 ;
    if ( result < 0 ) :
        result = ( result + 7 ) % 7 ;
    return result ;


def f_filled ( num ) :
    series = [ 1 , 3 , 2 , - 1 , - 3 , - 2 ]
    series_index = 0
    result = 0
    for i in range ( len ( num ) - 1 , - 1 , - 1 ) :
        digit = num [ i ] - '0'
        result += digit * series [ series_index ]
        series_index = ( series_index + 1 ) % 6
        result %= 7
    if result < 0 :
        result = ( result + 7 ) % 7
    return result

if __name__ == '__main__':
    param = [
    ('K',),
    ('850076',),
    ('00111',),
    ('X',),
    ('1',),
    ('10010001100',),
    (' pgPeLz',),
    ('53212456821275',),
    ('101',),
    ('V',)
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
