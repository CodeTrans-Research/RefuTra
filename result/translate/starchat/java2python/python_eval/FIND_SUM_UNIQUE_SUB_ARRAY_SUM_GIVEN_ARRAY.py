import sys
import math
import heapq
from queue import Queue# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( arr , n ) :
    res = 0
    m = dict ( )
    for i in range ( n ) :
        Sum = 0
        for j in range ( i , n ) :
            Sum += arr [ j ]
            m [ Sum ] = m.get ( Sum , 0 ) + 1
    for x in m :
        if m [ x ] == 1 :
            res += x
    return res


def f_filled(arr, n):
        res = 0
        m = {}
        for i in range(n):
            sum = 0
            for j in range(i, n):
                sum += arr[j]
                if sum in m:
                    m[sum] += 1
                else:
                    m[sum] = 1
        for x in m.items():
            if x[1] == 1:
                res += x[0]
        return res

if __name__ == '__main__':
    param = [
    ([7, 24, 34, 35, 36, 40, 49, 51, 53, 74, 78],9,),
    ([-34, 60, 32],2,),
    ([0],0,),
    ([80, 64, 10, 82, 14, 75, 51, 91, 1, 25, 98, 22, 36, 27, 21, 31, 93, 6, 52, 91, 80, 8, 62, 95, 10, 71, 40, 80, 35, 86, 85, 26, 74, 72, 64, 88, 4, 71, 4, 16],31,),
    ([-94, -46, -36, -24, -22, 0, 10, 14, 34, 34, 90, 92, 98],9,),
    ([1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1],21,),
    ([19, 20, 20, 24, 25, 33, 43, 47, 57, 61, 61, 64, 65, 71, 72, 73, 75, 82, 90, 93, 95],15,),
    ([-6, 56, 58, -36, 70, -92, 30, 58, -40, 98, 80, -96, -4, -88, 34, 76, 40, -32, -94, -26, 8, 72, -56, -96, -88, -24, 36, 14, -88, -32, 90, 4, -88, 28, 18],24,),
    ([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],11,),
    ([91, 51, 15, 78, 55, 3, 10, 24, 42, 84, 66, 78, 10, 41, 21, 53, 69, 57, 20, 22, 50, 72, 8, 80, 12, 91, 29, 95, 38, 74, 95, 26, 10, 57, 51, 25, 49, 74, 15, 42, 99, 21, 27],36,)
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
