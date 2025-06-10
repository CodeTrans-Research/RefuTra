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
    length = len ( num )
    if ( length == 1 and num [ 0 ] == '0' ) :
        return True
    if ( length % 3 == 1 ) :
        num = str ( num ) + "00"
        length += 2
    elif ( length % 3 == 2 ) :
        num = str ( num ) + "0"
        length += 1
    sum = 0
    p = 1
    for i in range ( length - 1 , - 1 , - 1 ) :
        group = 0
        group += ord ( num [ i ] ) - ord ( '0' )
        i -= 1
        group += ( ord ( num [ i ] ) - ord ( '0' ) ) * 10
        i -= 1
        group += ( ord ( num [ i ] ) - ord ( '0' ) ) * 100
        sum = sum + group * p
        p *= ( - 1 )
    sum = abs ( sum )
    return ( sum % 13 == 0 )


def f_filled ( num ) :
    length = len ( num )
    if length == 1 and num [ 0 ] == '0' :
        return True
    if length % 3 == 1 :
        num += '00'
        length += 2
    elif length % 3 == 2 :
        num += '0'
        length += 1
    sum , p = 0 , 1
    for i in range ( length - 1 , - 1 , - 1 ) :
        group = 0
        group += num [ i ] - '0'
        group += ( num [ i ] - '0' ) * 10
        group += ( num [ i ] - '0' ) * 100
        sum = sum + group * p
        p *= ( - 1 )
    sum = abs ( sum )
    return ( sum % 13 == 0 )

if __name__ == '__main__':
    param = [
    ('vzTUaItpCpLnjY',),
    ('33855',),
    ('0011110101011',),
    ('MMQ',),
    ('439340517954',),
    ('000000000',),
    ('UugAuRRJbjEgl',),
    ('6406553695441',),
    ('011001',),
    ('yjFqEEvgiNjEX',)
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
