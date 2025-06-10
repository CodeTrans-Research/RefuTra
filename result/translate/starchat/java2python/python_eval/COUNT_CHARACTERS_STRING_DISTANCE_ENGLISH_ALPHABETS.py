import sys
import math
import heapq
from queue import Queue# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( str1 ) :
    result = 0 ;
    n = len ( str1 )
    for i in range ( 0 , n ) :
        for j in range ( i + 1 , n ) :
            if ( abs ( ord ( str1 [ i ] ) - ord ( str1 [ j ] ) ) == abs ( i - j ) ) :
                result += 1 ;
    return result ;


def f_filled(str):
        result = 0
        n = len(str)
        for i in range(n):
            for j in range(i + 1, n):
                if abs(ord(str[i]) - ord(str[j])) == abs(i - j):
                    result += 1
        return result

if __name__ == '__main__':
    param = [
    ('smnKL',),
    ('270083',),
    ('0',),
    ('kcZdsz',),
    ('483544224',),
    ('000011',),
    ('WysGCirMwKBzP',),
    ('3366',),
    ('110',),
    ('NlaMkpCjUgg',)
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
