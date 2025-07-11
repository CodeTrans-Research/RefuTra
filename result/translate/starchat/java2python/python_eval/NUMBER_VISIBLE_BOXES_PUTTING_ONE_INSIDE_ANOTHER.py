import sys
import math
import heapq
from queue import Queue# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
import collections

def f_gold ( arr , n ) :
    q = collections.deque ( [ ] )
    arr = arr[:n]
    arr.sort ( )
    q.append ( arr [ 0 ] )
    for i in range ( 1 , n ) :
        now = q [ 0 ]
        if ( arr [ i ] >= 2 * now ) :
            q.popleft ( )
        q.append ( arr [ i ] )
    return len ( q )


def f_filled(arr, n):
        arr.sort()
        q = []
        for i in range(n):
            while q and arr[i] >= 2 * q[-1]:
                q.pop()
            q.append(arr[i])
        return len(q)

if __name__ == '__main__':
    param = [
    ([2, 3, 17, 17, 18, 28, 28, 29, 34, 43, 44, 52, 54, 80, 84, 84, 91, 92, 97],12,),
    ([-34, 70, -90, -10, -26, 64, 4, 28, 24, -90, -78, 72, 74, 80, 82, -94],10,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],40,),
    ([20, 87, 5, 62, 12, 81, 30, 83, 96, 16, 2, 76, 3, 8, 37, 53, 55, 88],9,),
    ([-94, -92, -60, -58, -54, -42, -36, -12, -8, -2, 8, 14, 18, 20, 26, 32, 38, 56, 58, 60, 70, 78, 80, 86, 98],18,),
    ([0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],9,),
    ([1, 1, 2, 3, 3, 11, 16, 18, 19, 21, 21, 22, 22, 24, 27, 28, 29, 43, 43, 52, 55, 57, 60, 62, 62, 63, 65, 66, 70, 70, 73, 77, 78, 79, 79, 80, 85, 85, 86, 88, 89, 90, 97, 98],30,),
    ([88, 12, -22, -60, 30, -30, -14, 80, -58, -80, -10, 86, -94, -14, 4, -18, -18, 54, -82, -8, -68, -6, -44, -44, 50, 88, -78, -42, 12, 52, 44, 14, 6, 48, 18, -30, 4],21,),
    ([0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],7,),
    ([82, 62, 43, 39, 5, 90, 75, 50, 16, 83, 52, 69, 71, 3, 89, 10, 51, 69, 32, 96, 5, 43, 83, 12, 31, 81, 22, 59, 52, 47, 86, 49, 56, 90, 31, 59],28,)
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

