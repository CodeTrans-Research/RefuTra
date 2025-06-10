import sys
import math
import heapq
from queue import Queue# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( a , b ) :
    n = len ( a )
    m = len ( b )
    if m == 0 :
        return 1
    dp = [ [ 0 ] * ( n + 1 ) for _ in range ( m + 1 ) ]
    for i in range ( m ) :
        for j in range ( i , n ) :
            if i == 0 :
                if j == 0 :
                    if a [ j ] == b [ i ] :
                        dp [ i ] [ j ] = 1
                    else :
                        dp [ i ] [ j ] = 0
                elif a [ j ] == b [ i ] :
                    dp [ i ] [ j ] = dp [ i ] [ j - 1 ] + 1
                else :
                    dp [ i ] [ j ] = dp [ i ] [ j - 1 ]
            else :
                if a [ j ] == b [ i ] :
                    dp [ i ] [ j ] = ( dp [ i ] [ j - 1 ] + dp [ i - 1 ] [ j - 1 ] )
                else :
                    dp [ i ] [ j ] = dp [ i ] [ j - 1 ]
    return dp [ m - 1 ] [ n - 1 ]


def f_filled(a, b):
        n = len(a)
        m = len(b)
        if m == 0:
            return 1
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0:
                    if j == 0:
                        dp[i][j] = (a[j] == b[i]) * 1
                    else:
                        if a[j] == b[i]:
                            dp[i][j] = dp[i][j - 1] + 1
                        else:
                            dp[i][j] = dp[i][j - 1]
                else:
                    if j == 0:
                        if a[j] == b[i - 1]:
                            dp[i][j] = dp[i - 1][j] + 1
                        else:
                            dp[i][j] = dp[i - 1][j]
                    else:
                        if a[j] == b[i - 1] and b[i]

if __name__ == '__main__':
    param = [
    ('abcccdf','abccdf',),
    ('aabba','ab',),
    ('aabsdfljk','aa',),
    ('IONiqV','XKbBiGZ',),
    ('9667771256770','50915176',),
    ('10001011','01',),
    ('fczbDtMDT','FbX',),
    ('298746088','29888',),
    ('01100011000','0',),
    ('Qk','',)
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
