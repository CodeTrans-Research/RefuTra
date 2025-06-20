import sys
import math
import heapq
from queue import Queue# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( degree , n ) :
    deg_sum = 0
    for i in range(n):
        deg_sum += degree[i]
    if ( 2 * ( n - 1 ) == deg_sum ) :
        return True
    else :
        return False


def f_filled(degree, n):
        deg_sum = sum(degree)
        return 2 * (n - 1) == deg_sum

if __name__ == '__main__':
    param = [
    ([2, 3, 1, 1, 1],5,),
    ([2, 2, 1, 1, 2],5,),
    ([2, 2, 1, 1, 1],5,),
    ([0,0,0,3,3,4],6,),
    ([-10, 12, 2],3,),
    ([1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0],19,),
    ([1, 6, 10, 13, 15, 17, 18, 23, 26, 28, 30, 32, 32, 33, 36, 39, 39, 41, 43, 50, 50, 51, 53, 54, 59, 59, 63, 63, 63, 66, 66, 71, 71, 74, 78, 89, 89, 93],30,),
    ([66, -96, -14, 74, -20],4,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],31,),
    ([97, 73, 87, 45, 64, 30, 53, 50, 62, 42, 28, 58, 31, 90],10,)
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
