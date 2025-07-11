import sys
import math
import heapq
from queue import Queue
# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( arr , n , x ) :
    for i in range ( n ) :
        if arr [ i ] > arr [ i + 1 ] :
            break
    l = ( i + 1 ) % n
    r = i
    cnt = 0
    while ( l != r ) :
        if arr [ l ] + arr [ r ] == x :
            cnt += 1
            if l == ( r - 1 + n ) % n :
                return cnt
            l = ( l + 1 ) % n
            r = ( r - 1 + n ) % n
        elif arr [ l ] + arr [ r ] < x :
            l = ( l + 1 ) % n
        else :
            r = ( n + r - 1 ) % n
    return cnt


def f_filled(arr, n, x):
    i = 0
    while i < n - 1:
        if arr[i] > arr[i + 1]:
            break
        i += 1
    
    l = (i + 1) % n
    r = i
    cnt = 0
    
    while l != r:
        if arr[l] + arr[r] == x:
            cnt += 1
            if l == (r - 1 + n) % n:
                return cnt
            l = (l + 1) % n
            r = (r - 1 + n) % n
        elif arr[l] + arr[r] < x:
            l = (l + 1) % n
        else:
            r = (n + r - 1) % n
    
    return cnt

if __name__ == '__main__':
    param = [
    ([24, 54],1,1,),
    ([68, -30, -18, -6, 70, -40, 86, 98, -24, -48],8,8,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],33,28,),
    ([84, 44, 40, 45, 2, 41, 52, 17, 50, 41, 5, 52, 48, 90, 13, 55, 34, 55, 94, 44, 41, 2],18,16,),
    ([-92, -76, -74, -72, -68, -64, -58, -44, -44, -38, -26, -24, -20, -12, -8, -8, -4, 10, 10, 10, 20, 20, 26, 26, 28, 50, 52, 54, 60, 66, 72, 74, 78, 78, 78, 80, 86, 88],29,30,),
    ([1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1],19,10,),
    ([5, 5, 15, 19, 22, 24, 26, 27, 28, 32, 37, 39, 40, 43, 49, 52, 55, 56, 58, 58, 59, 62, 67, 68, 77, 79, 79, 80, 81, 87, 95, 95, 96, 98, 98],28,34,),
    ([-98, 28, 54, 44, -98, -70, 48, -98, 56, 4, -18, 26, -8, -58, 30, 82, 4, -38, 42, 64, -28],17,14,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],24,24,),
    ([26, 72, 74, 86, 98, 86, 22, 6, 95, 36, 11, 82, 34, 3, 50, 36, 81, 94, 55, 30, 62, 53, 50, 95, 32, 83, 9, 16],19,16,)
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
            if set([filledres,goldres]) == set([float("inf"),sys.maxsize]) or set([filledres,goldres]) <= set([float("-inf"),-sys.maxsize-1,-sys.maxsize]):
                n_success += 1
    print("#Results: %i, %i" % (n_success, len(param)))
