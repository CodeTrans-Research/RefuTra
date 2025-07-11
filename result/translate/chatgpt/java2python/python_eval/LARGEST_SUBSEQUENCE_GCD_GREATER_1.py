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
    ans = 0
    maxele = max ( arr )
    for i in range ( 2 , maxele + 1 ) :
        count = 0
        for j in range ( n ) :
            if ( arr [ j ] % i == 0 ) :
                count += 1
        ans = max ( ans , count )
    return ans


def f_filled(arr, n):
    ans = 0
    maxele = max(arr)
    
    for i in range(2, maxele+1):
        count = 0
        for j in range(n):
            if arr[j] % i == 0:
                count += 1
        ans = max(ans, count)
    
    return ans

if __name__ == '__main__':
    param = [
    ([10, 18, 22, 22, 22, 29, 30, 32, 33, 34, 37, 39, 40, 41, 44, 47, 49, 50, 50, 51, 53, 67, 69, 70, 71, 71, 73, 75, 78, 80, 81, 82, 91, 91, 93, 97, 97, 99],35,),
    ([-42, 62, 6, 98, 38, -4, -38, 72, 42, 4, -22, -94, 78, -90, 14],10,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],23,),
    ([89, 92, 96, 71, 24, 27, 18, 19, 41, 1, 45, 8],7,),
    ([-98, -94, -92, -90, -82, -80, -76, -76, -72, -62, -60, -58, -56, -52, -42, -36, -32, -32, -24, -22, -20, -10, -10, -10, -8, -2, -2, 0, 2, 4, 6, 6, 8, 10, 14, 18, 22, 26, 30, 46, 46, 62, 68, 74, 78, 82, 86, 86],40,),
    ([1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],41,),
    ([4, 8, 10, 10, 11, 17, 18, 25, 32, 33, 34, 37, 40, 41, 44, 47, 47, 52, 63, 77, 85, 87, 89, 89, 91, 95, 96, 98],23,),
    ([-86, 52, -48, 70, 10, -94, 16, 14, 38, 62],9,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],30,),
    ([95, 32, 87, 37, 86, 71, 30, 88, 96, 52, 88, 92, 79, 86, 19, 5, 74, 67],13,)
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
