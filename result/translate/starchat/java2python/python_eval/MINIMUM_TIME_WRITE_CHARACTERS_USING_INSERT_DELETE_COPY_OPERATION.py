import sys
import math
import heapq
from queue import Queue# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( N , insrt , remov , cpy ) :
    if N == 0 :
        return 0
    if N == 1 :
        return insrt
    dp = [ 0 ] * ( N + 1 )
    for i in range ( 1 , N + 1 ) :
        if i % 2 == 0 :
            dp [ i ] = min ( dp [ i - 1 ] + insrt , dp [ i // 2 ] + cpy )
        else :
            dp [ i ] = min ( dp [ i - 1 ] + insrt , dp [ ( i + 1 ) // 2 ] + cpy + remov )
    return dp [ N ]


def f_filled(N, insert, remove, copy):
        if N == 0:
            return 0
        if N == 1:
            return insert
        dp = [0] * (N + 1)
        for i in range(1, N + 1):
            if i % 2 == 0:
                dp[i] = min(dp[i - 1] + insert, dp[i // 2] + copy)
            else:
                dp[i] = min(dp[i - 1] + insert, dp[(i + 1) // 2] + copy + remove)
        return dp[N]

if __name__ == '__main__':
    param = [
    (59,75,12,45,),
    (66,68,32,41,),
    (98,55,69,5,),
    (63,4,41,12,),
    (99,37,98,55,),
    (45,28,59,7,),
    (60,53,40,52,),
    (11,96,50,50,),
    (96,95,48,84,),
    (54,6,50,82,)
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
