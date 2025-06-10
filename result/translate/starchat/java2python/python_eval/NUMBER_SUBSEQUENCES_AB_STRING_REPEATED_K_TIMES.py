import sys
import math
import heapq
from queue import Queue# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( s , K ) :
    n = len ( s )
    c1 = 0
    c2 = 0
    C = 0
    for i in range ( n ) :
        if s [ i ] == 'a' :
            c1 += 1
        if s [ i ] == 'b' :
            c2 += 1
            C += c1
    return C * K + K * ( K - 1 ) // 2 * c1 * c2


def f_filled(s, K):
        n = len(s)
        C = 0
        c1 = 0
        c2 = 0
        for i in range(n):
            if s[i] == 'a':
                c1 += 1
            if s[i] == 'b':
                c2 += 1
                C += c1
        return C * K + (K * (K - 1) // 2) * c1 * c2

if __name__ == '__main__':
    param = [
   ('abbc',10**10,),
('abahk',7,),
('hugbabab',59,),
('abadbc',60,),
('nkg9',8,),
('jh7dab',41,),
('abd',87,),
('aabb8yk',4,),
('1111',18,),
('PFXAhr',8,)
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

