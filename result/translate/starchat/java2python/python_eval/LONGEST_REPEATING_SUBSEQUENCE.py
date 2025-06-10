import sys
import math
import heapq
from queue import Queue# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( str ) :
    n = len ( str )
    dp = [ [ 0 ] * ( n + 1 ) ] * ( n + 1 )
    for i in range ( 1 , n + 1 ) :
        for j in range ( 1 , n + 1 ) :
            if ( str [ i - 1 ] == str [ j - 1 ] and i != j ) :
                dp [ i ] [ j ] = 1 + dp [ i - 1 ] [ j - 1 ]
            else :
                dp [ i ] [ j ] = max ( dp [ i ] [ j - 1 ] , dp [ i - 1 ] [ j ] )
    return dp [ n ] [ n ]


def f_filled(str):
        n = len(str)
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, n+1):
                if str[i-1] == str[j-1] and i!= j:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return dp[n][n]

if __name__ == '__main__':
    param = [
    ('JxZFz',),
    ('7648992235770',),
    ('11100000',),
    ('cRN  SgYjPsctJ',),
    ('434',),
    ('1',),
    ('JRfZIAsbrPBZ',),
    ('03779368305592',),
    ('1111000',),
    ('BkULuIi',)
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
