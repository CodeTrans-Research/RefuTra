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
def f_gold ( arr , n ) :
    arr.sort ( )
    count = 0 ; max_count = 0 ; min_count = n
    for i in range ( 0 , ( n - 1 ) ) :
        if arr [ i ] == arr [ i + 1 ] :
            count += 1
            continue
        else :
            max_count = max ( max_count , count )
            min_count = min ( min_count , count )
            count = 0
    return max_count - min_count


def f_filled(arr, n):
    arr.sort()
    count = 0
    max_count = 0
    min_count = n
    
    for i in range(n - 1):
        if arr[i] == arr[i + 1]:
            count += 1
            continue
        else:
            max_count = max(max_count, count)
            min_count = min(min_count, count)
            count = 0
            
    return max_count - min_count

if __name__ == '__main__':
    param = [
    ([5, 15, 19, 22, 28, 29, 39, 46, 46, 49, 51, 55, 62, 69, 72, 72, 72, 74, 79, 92, 92, 93, 95, 96],15,),
    ([-26, -54, 92, 76, -92, -14, -24, -70, -78, -50, -48, -22, 12, 2, -34, -60, 4, -32, -10, 52, -92, -74, 18, 34, 6, -66, 42, -10, -6, 56, 92],30,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],24,),
    ([59, 35, 13, 79, 61, 97, 92, 48, 98, 38, 65, 54, 31, 49, 81, 22, 96, 29, 65, 48, 92, 66, 25, 21, 26, 1, 32, 73, 46, 5, 40, 17, 53, 93, 83, 29],29,),
    ([-70, -34, -32, -30, -14, 80, 86, 90],4,),
    ([0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0],23,),
    ([9],0,),
    ([94, 10, 70, 42],2,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],24,),
    ([64, 76, 49, 55, 92, 15, 4, 8, 95, 60, 90, 3, 7, 79, 84, 17, 96, 10, 80, 26, 22, 15],20,)
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
