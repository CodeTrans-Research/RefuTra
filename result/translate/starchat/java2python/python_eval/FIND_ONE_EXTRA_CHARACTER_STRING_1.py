import sys
import math
import heapq
from queue import Queue# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( strA , strB ) :
    res = 0
    for i in range ( 0 , len ( strA ) ) :
        res = res ^ ( ord ) ( strA [ i ] )
    for i in range ( 0 , len ( strB ) ) :
        res = res ^ ( ord ) ( strB [ i ] )
    return ( ( chr ) ( res ) ) ;


def f_filled(strA, strB):
        res = 0
        for i in range(len(strA)):
            res ^= ord(strA[i])
        for i in range(len(strB)):
            res ^= ord(strB[i])
        return chr(res)

if __name__ == '__main__':
    param = [
    ('obfLA mmMYvghH','obfLA  mmMYvghH',),
    ('2941','2941',),
    ('0111111','0111111',),
    ('oWvbFstI','oWvbFstI',),
    ('4937516500','4937516500',),
    ('101110100','101110100',),
    ('hYZscJQFBE','hYZscJQFBE',),
    ('58443','58443',),
    ('1100','1100',),
    ('ZUdYuIBVNaeeb','ZUdYuIBVNaeeb',)
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
