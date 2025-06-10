import sys
import math
import heapq
from queue import Queue# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( n ) :
    ans = 0 ; temp = 0 ;
    for i in range ( 1 , n + 1 ) :
        if temp < n :
            temp = i - 1
            num = 1
            while temp < n :
                if temp + i <= n :
                    ans += i * num
                else :
                    ans += ( n - temp ) * num
                temp += i
                num += 1
    return ans


def f_filled(n):
        ans, temp, num = 0, 0, 1
        for i in range(1, n + 1):
            temp = i - 1
            num = 1
            while temp < n:
                if temp + i <= n:
                    ans += i * num
                else:
                    ans += (n - temp) * num
                temp += i
                num += 1
        return ans

if __name__ == '__main__':
    param = [
    (35,),
    (93,),
    (7,),
    (81,),
    (80,),
    (47,),
    (7,),
    (41,),
    (59,),
    (34,)
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
