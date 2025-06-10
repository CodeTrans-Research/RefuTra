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
def f_gold ( arr , l , r , x ) :
    if ( r >= l ) :
        mid = int ( l + ( r - l ) / 2 )
        if ( arr [ mid ] == x ) : return mid
        if ( mid > l and arr [ mid - 1 ] == x ) :
            return ( mid - 1 )
        if ( mid < r and arr [ mid + 1 ] == x ) :
            return ( mid + 1 )
        if ( arr [ mid ] > x ) :
            return f_gold ( arr , l , mid - 2 , x )
        return f_gold ( arr , mid + 2 , r , x )
    return - 1


def f_filled(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        if mid > l and arr[mid - 1] == x:
            return mid - 1
        if mid < r and arr[mid + 1] == x:
            return mid + 1
        if arr[mid] > x:
            return f_filled(arr, l, mid - 2, x)
        return f_filled(arr, mid + 2, r, x)
    
    return -1

if __name__ == '__main__':
    param = [
    ([6,7,15,42,47,54,56,59,59,64,68,70,71,75,91,93], 0, 15, 71),
([6,7,15,42,47,56,54,59,59,64,68,71,70, 75,91,93], 0, 15,    71),
([-92,-96,-68,-40,70], 0, 4,    -96),
([-92,-86,-68,-40,70], 0, 4,    20),
([-3,-1,0,30,10,45,70,60], 0, 7,    0),
([-3,-1,0,10,5,45,60,50], 0, 7,    12),
([-3,-1,0,10,30,45,60,70], 0, 7,    18),
([0,0,1], 0, 2,    20),
([1,1,1], 0, 2,    17),
([30,2,30,45], 0, 3,    28)
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

