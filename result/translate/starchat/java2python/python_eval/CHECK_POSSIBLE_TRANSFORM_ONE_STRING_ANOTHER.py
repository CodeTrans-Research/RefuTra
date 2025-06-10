import sys
import math
import heapq
from queue import Queue# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( s1 , s2 ) :
    n = len ( s1 )
    m = len ( s2 )
    dp = ( [ [ False for i in range ( m + 1 ) ] for i in range ( n + 1 ) ] )
    dp [ 0 ] [ 0 ] = True
    for i in range ( len ( s1 ) ) :
        for j in range ( len ( s2 ) + 1 ) :
            if ( dp [ i ] [ j ] ) :
                if ( ( j < len ( s2 ) and ( s1 [ i ].upper ( ) == s2 [ j ] ) ) ) :
                    dp [ i + 1 ] [ j + 1 ] = True
                if ( s1 [ i ].isupper ( ) == False ) :
                    dp [ i + 1 ] [ j ] = True
    return ( dp [ n ] [ m ] )


def f_filled(s1, s2):
        n = len(s1)
        m = len(s2)
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            for j in range(m + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] and (s2[j - 1].isupper() or s1[i - 1] == s2[j - 1])
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] and (s1[i - 1].isupper() or s1[i - 1] == s2[j - 1])
                else:
                    dp[i][j] = dp[i - 1][j] and (s1[i - 1] == s2[j - 1]) or (dp[i][j - 1] and (s

if __name__ == '__main__':
    param = [
    ('daBcd','ABC',),
    ('417514','9',),
    ('010000','1111011010',),
    ('ZcKYguiMrdyn','iz',),
    ('argaju','RAJ',),
    ('1110101101','110101001',),
    ('ySOCoSaygi','aRhxkYqh',),
    ('204','6986871066',),
    ('10011100000010','0',),
    ('nMAioozPmY','WZFdDKw',)
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
