import sys
import math
import heapq
from queue import Queue# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( n ) :
    result = 0
    for i in range ( 1 , 10 ) :
        s = [ ]
        if ( i <= n ) :
            s.append ( i )
            result += 1
        while len ( s ) != 0 :
            tp = s [ - 1 ]
            s.pop ( )
            for j in range ( tp % 10 , 10 ) :
                x = tp * 10 + j
                if ( x <= n ) :
                    s.append ( x )
                    result += 1
    return result


def f_filled(n):
        result = 0
        for i in range(1, 10):
            stack = []
            if i <= n:
                stack.append(i)
                result += 1
            while stack:
                top = stack.pop()
                for j in range(top % 10, 10):
                    x = top * 10 + j
                    if x <= n:
                        stack.append(x)
                        result += 1
        return result

if __name__ == '__main__':
    param = [
    (69,),
    (72,),
    (88,),
    (7,),
    (66,),
    (34,),
    (23,),
    (37,),
    (33,),
    (21,)
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
