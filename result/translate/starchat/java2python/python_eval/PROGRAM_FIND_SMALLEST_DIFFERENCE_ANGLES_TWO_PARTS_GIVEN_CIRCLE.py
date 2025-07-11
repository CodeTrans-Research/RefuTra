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
    l = 0
    _sum = 0
    ans = 360
    for i in range ( n ) :
        _sum += arr [ i ]
        while _sum >= 180 :
            ans = min ( ans , 2 * abs ( 180 - _sum ) )
            _sum -= arr [ l ]
            l += 1
        ans = min ( ans , 2 * abs ( 180 - _sum ) )
    return ans


def f_filled(arr, n):
        l, sum, ans = 0, 0, 360
        for i in range(n):
            sum += arr[i]
            while sum >= 180:
                ans = min(ans, 2 * abs(180 - sum))
                sum -= arr[l]
                l += 1
            ans = min(ans, 2 * abs(180 - sum))
        return ans

if __name__ == '__main__':
    param = [
    ([4, 4, 5, 5, 13, 14, 14, 16, 19, 20, 30, 31, 32, 33, 35, 38, 38, 42, 44, 44, 48, 48, 52, 58, 60, 64, 65, 66, 68, 69, 70, 70, 71, 72, 73, 79, 81, 83, 83, 84, 86, 87, 88, 88, 91, 92, 95, 95, 98],27,),
    ([-56, 88, -50, 70, 20, 58, 42, -56, -52, -78, 98, 20, -26, 4, 20, -66, -46, -58, 74, 74, -72, 2, 16, -78, -4, 10, 58, 60, -46, -2, 32, -96, 24, -6, 90, -64, -24, -38, 26, 66, -42, -86, 48, 92, 28, 6, -54, -6],29,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],25,),
    ([52, 67, 62],1,),
    ([-56, -22, 32, 42, 66],4,),
    ([1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0],10,),
    ([38, 46, 58, 72],2,),
    ([16, 62, 90, 40, 30, -56, -92, -56, 60, 42, -64, 92, -30, -70, 42, -48, -54, 54, 48, 94, -44, -46, 10, 48, 22, -24, -62, 34, 60, 24, -60, 50, 40, 34],20,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],37,),
    ([86, 43, 74, 84, 86, 14, 45, 7, 92, 36, 79, 13, 67, 18, 96, 77, 13, 22, 28, 36, 57, 56, 99, 57, 8, 48, 5, 79, 65, 64, 96, 6, 36, 91, 53, 55, 11, 12, 80, 99, 50, 40, 4, 9, 52, 41],40,)
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
