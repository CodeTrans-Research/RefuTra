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
def f_gold ( n ) :
    num = n ;
    dec_value = 0 ;
    base1 = 1 ;
    len1 = len ( num ) ;
    for i in range ( len1 - 1 , - 1 , - 1 ) :
        if ( num [ i ] == '1' ) :
            dec_value += base1 ;
        base1 = base1 * 2 ;
    return dec_value ;


def f_filled(n):
    num = n
    dec_value = 0
    base = 1
    len_num = len(num)
    
    for i in range(len_num - 1, -1, -1):
        if num[i] == '1':
            dec_value += base
        base *= 2

    return dec_value

if __name__ == '__main__':
    param = [
    ('uEmIAgF',),
    ('753310137',),
    ('010011010',),
    ('kNi',),
    ('04562016903312',),
    ('000111101',),
    ('bk',),
    ('9',),
    ('1',),
    ('XxT nXLlk',)
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
