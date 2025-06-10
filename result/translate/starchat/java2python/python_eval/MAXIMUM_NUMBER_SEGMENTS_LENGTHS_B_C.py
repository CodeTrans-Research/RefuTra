import sys
import math
import heapq
from queue import Queue# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( n , a , b , c ) :
    dp = [ - 1 ] * ( n + 10 )
    dp [ 0 ] = 0
    for i in range ( 0 , n ) :
        if ( dp [ i ] != - 1 ) :
            if ( i + a <= n ) :
                dp [ i + a ] = max ( dp [ i ] + 1 , dp [ i + a ] )
            if ( i + b <= n ) :
                dp [ i + b ] = max ( dp [ i ] + 1 , dp [ i + b ] )
            if ( i + c <= n ) :
                dp [ i + c ] = max ( dp [ i ] + 1 , dp [ i + c ] )
    return dp [ n ]


def f_filled(n, a, b, c):
        dp = [-1] * (n + 10)
        dp[0] = 0
        for i in range(n):
            if dp[i]!= -1:
                if i + a <= n:
                    dp[i + a] = max(dp[i] + 1, dp[i + a])
                if i + b <= n:
                    dp[i + b] = max(dp[i] + 1, dp[i + b])
                if i + c <= n:
                    dp[i + c] = max(dp[i] + 1, dp[i + c])
        return dp[n]

if __name__ == '__main__':
    param = [
    (23,16,23,18,),
    (62,76,81,97,),
    (32,46,1,78,),
    (82,48,72,58,),
    (94,99,62,38,),
    (44,21,46,60,),
    (4,57,2,77,),
    (53,23,80,5,),
    (9,55,26,85,),
    (23,15,73,42,)
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
