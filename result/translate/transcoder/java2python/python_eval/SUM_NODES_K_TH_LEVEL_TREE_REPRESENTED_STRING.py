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
def f_gold ( tree , k ) :
    level = - 1
    sum = 0
    n = len ( tree )
    for i in range ( n ) :
        if ( tree [ i ] == '(' ) :
            level += 1
        elif ( tree [ i ] == ')' ) :
            level -= 1
        else :
            if ( level == k ) :
                sum += ( ord ( tree [ i ] ) - ord ( '0' ) )
    return sum


def f_filled ( tree , k ) :
    level = - 1
    sum = 0
    n = len ( tree )
    for i in range ( n ) :
        if tree [ i ] == '(' :
            level += 1
        elif tree [ i ] == ')' :
            level -= 1
        else :
            if level == k :
                sum += ( tree [ i ] - '0' )
    return sum

if __name__ == '__main__':
    param = [
    ('(0(5(6()())(4()(9()())))(7(1()())(3()())))',2,),
    ('(8(3(2()())(6(5()())()))(5(10()())(7(13()())())))',3,),
    ('(0(5(6()())(4()(9()())))(7(1()())(3()())))',1,),
    ('(8(3(2()())(6(5()())()))(5(10()())(7(13()())())))',2,),
    ('(8(3(2()())(6(5()())()))(5(10()())(7(13()())())))',4,),
    ('(8(3(2()())(6(5()())()))(5(10()())(7(13()())())))',100,),
    ('(0(5(6()())(4()(9()())))(7(1()())(3()())))',3,),
    ('(0(5(6()())(4()(9()())))(7(1()())(3()())))',0,),
    ('0010',12,),
    ('kjtdgmy',97,)
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
