import sys
import math
import heapq
from queue import Queue# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( s ) :
    n = len ( s )
    lps = [ 0 ] * n
    l = 0
    i = 1
    while ( i < n ) :
        if ( s [ i ] == s [ l ] ) :
            l = l + 1
            lps [ i ] = l
            i = i + 1
        else :
            if ( l != 0 ) :
                l = lps [ l - 1 ]
            else :
                lps [ i ] = 0
                i = i + 1
    res = lps [ n - 1 ]
    if ( res > n / 2 ) :
        return n // 2
    else :
        return res


def f_filled(s):
        n = len(s)
        lps = [0] * n
        lps[0] = 0
        len = 0
        i = 1
        while i < n:
            if s[i] == s[len]:
                len += 1
                lps[i] = len
                i += 1
            else:
                if len!= 0:
                    len = lps[len - 1]
                else:
                    lps[i] = 0
                    i += 1
        res = lps[n - 1]
        return max(res, n // 2)

if __name__ == '__main__':
    param = [
    ('aabcdaabc',),
    ('1372494598',),
    ('110000100001',),
    ('abcab',),
    ('488938',),
    ('011010101011',),
    ('aaaa',),
    ('3356203205',),
    ('1010',),
    ('kkXiiTZkGeh',)
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
