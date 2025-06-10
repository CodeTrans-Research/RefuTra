import sys
import math
import heapq
from queue import Queue# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( n , k ) :
    dp = [ [ 0 for i in range ( k + 1 ) ] for j in range ( n + 1 ) ]
    for i in range ( n + 1 ) :
        dp [ i ] [ 0 ] = 0
    for i in range ( k + 1 ) :
        dp [ 0 ] [ k ] = 0
    for i in range ( 1 , n + 1 ) :
        for j in range ( 1 , k + 1 ) :
            if ( j == 1 or i == j ) :
                dp [ i ] [ j ] = 1
            else :
                dp [ i ] [ j ] = ( j * dp [ i - 1 ] [ j ] + dp [ i - 1 ] [ j - 1 ] )
    return dp [ n ] [ k ]


def f_filled(n, k):
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            for j in range(k + 1):
                if j == 0 or i == j:
                    dp[i][j] = 0
                elif j == 1:
                    dp[i][j] = i
                else:
                    dp[i][j] = j * dp[i - 1][j] + dp[i - 1][j - 1]
        return dp[n][k]

if __name__ == '__main__':
    param = [
    (84,99,),
    (95,64,),
    (67,21,),
    (92,22,),
    (97,35,),
    (13,77,),
    (37,46,),
    (9,92,),
    (10,26,),
    (90,94,)
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
