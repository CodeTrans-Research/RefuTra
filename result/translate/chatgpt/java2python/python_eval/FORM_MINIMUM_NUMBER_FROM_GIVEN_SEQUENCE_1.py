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
def f_gold ( seq ) :
    n = len ( seq )
    if ( n >= 9 ) :
        return "-1"
    result = [ '' ] * ( n + 1 )
    count = 1
    for i in range ( n + 1 ) :
        if ( i == n or seq [ i ] == 'I' ) :
            for j in range ( i - 1 , - 2 , - 1 ) :
                result [ j + 1 ] =  chr ( ord ( '0' ) + count)
                count += 1
                if ( j >= 0 and seq [ j ] == 'I' ) :
                    break
    return ''.join(result)

def f_filled(seq):
    n = len(seq)
    if n >= 9:
        return "-1"
    result = [''] * (n + 1)
    count = 1
    i = 0
    while i <= n:
        if i == n or seq[i] == 'I':
            j = i - 1
            while j >= -1:
                result[j + 1] = chr(ord('0') + count)
                count += 1
                if j >= 0 and seq[j] == 'I':
                    break
                j -= 1
        i += 1
    return ''.join(result)

if __name__ == '__main__':
    param = [
    ('D',),
    ('I',),
    ('DD',),
    ('II',),
    ('DIDI',),
    ('IIDDD',),
    ('DDIDDIID',),
    ('176297',),
    ('1',),
    ('XHkhZq',)
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
