import sys
import math
import heapq
from queue import Queue# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( h ) :
    MOD = 1000000007
    dp = [ 0 for i in range ( h + 1 ) ]
    dp [ 0 ] = 1
    dp [ 1 ] = 1
    for i in range ( 2 , h + 1 ) :
        dp [ i ] = ( dp [ i - 1 ] * ( ( 2 * dp [ i - 2 ] ) % MOD + dp [ i - 1 ] ) % MOD ) % MOD
    return dp [ h ]


def f_filled(h):
        MOD = 1000000007
        dp = [0] * (h + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, h + 1):
            dp[i] = (dp[i - 1] * (((2 * dp[i - 2]) % MOD + dp[i - 1]) % MOD)) % MOD
        return dp[h]

if __name__ == '__main__':
    param = [
    (75,),
    (50,),
    (93,),
    (87,),
    (35,),
    (25,),
    (43,),
    (61,),
    (54,),
    (91,)
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
