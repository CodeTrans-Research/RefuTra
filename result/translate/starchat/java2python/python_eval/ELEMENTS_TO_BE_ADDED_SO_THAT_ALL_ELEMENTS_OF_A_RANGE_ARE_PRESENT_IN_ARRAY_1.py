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
    s = dict ( )
    count , maxm , minm = 0 , - 10 ** 9 , 10 ** 9
    for i in range ( n ) :
        s [ arr [ i ] ] = 1
        if ( arr [ i ] < minm ) :
            minm = arr [ i ]
        if ( arr [ i ] > maxm ) :
            maxm = arr [ i ]
    for i in range ( minm , maxm + 1 ) :
        if i not in s.keys ( ) :
            count += 1
    return count


def f_filled(arr, n):
        s = set()
        count = 0
        maxm, minm = float("-inf"), float("inf")
        for i in range(n):
            s.add(arr[i])
            if arr[i] < minm:
                minm = arr[i]
            if arr[i] > maxm:
                maxm = arr[i]
        for i in range(int(minm), int(maxm)+1):
            if i not in s:
                count += 1
        return count

if __name__ == '__main__':
    param = [
    ([1, 4, 5, 5, 11, 11, 12, 14, 16, 20, 23, 23, 25, 27, 29, 33, 33, 35, 37, 39, 39, 44, 44, 45, 47, 51, 51, 53, 55, 65, 73, 73, 75, 78, 79, 79, 80, 82, 86, 86, 87, 87, 88, 90, 91, 91, 94],26,),
    ([-38, 20, -94, -68, -96, 36, 48, 32, 44, -56, 72, -28, -6, 22, -54, -46, 58, -60, -80, 28, -34, 60, -12, -26, -32, 28, 72, -50, 66, -36, 28, 30, 10, 14, 0, -78, 94, -24, -42, -60, 66, -12, 92, 54, -34, -58, 56],31,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],20,),
    ([73, 69, 12, 82, 65, 55, 93, 93, 88, 52, 33, 94, 62, 75, 61, 81, 48, 43, 29, 8, 28, 60, 60, 58, 54, 44, 25, 36, 46, 88, 54, 36, 83, 46, 34, 44, 71, 90, 68, 75, 42],31,),
    ([-98, -94, -88, -80, -74, -70, -70, -56, -50, -48, -40, -24, -22, -14, 0, 2, 2, 6, 12, 22, 30, 32, 32, 40, 48, 52, 52, 58, 64, 66, 66, 68, 70, 72, 74, 76, 78, 94, 98, 98],22,),
    ([1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1],18,),
    ([1, 2, 3, 4, 7, 11, 12, 13, 14, 15, 20, 21, 22, 25, 25, 28, 32, 32, 35, 36, 37, 38, 42, 42, 45, 48, 48, 48, 54, 67, 70, 70, 71, 74, 80, 81, 82, 82, 85, 94],24,),
    ([-90, 92, 28, -32, 76, 94, 48, 80, 52, -12, -6, 22, 40, 26, -18, -84, 90, 16, -76, 52, 10, -56, 6],11,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],14,),
    ([4, 21, 34, 35, 71, 10, 88, 44, 82, 13, 79, 92, 35, 73, 28, 91, 33, 9, 12, 76, 40, 91, 4, 22, 90, 53, 98, 7, 30],17,)
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
