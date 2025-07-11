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
import sys

def f_gold ( arr , n ) :
    res = - sys.maxsize
    for i in range ( 0 , n ) :
        curr_sum = 0
        for j in range ( 0 , n ) :
            index = int ( ( i + j ) % n )
            curr_sum += j * arr [ index ]
        res = max ( res , curr_sum )
    return res


def f_filled(arr, n):
    res = float('-inf')
    for i in range(n):
        curr_sum = 0
        for j in range(n):
            index = (i + j) % n
            curr_sum += j * arr[index]
        res = max(res, curr_sum)
    return res

if __name__ == '__main__':
    param = [
    ([11, 12, 16, 26, 29, 40, 54, 59, 65, 70, 71, 73, 78, 81, 87, 87, 88, 90, 95, 97],11,),
    ([-46, -32, 54, 96, -72, -58, -36, -44, 26, -2, -68, 42, 90, 26, -92, -96, 88, -42, -18, 46, -70, 24, 0, 24, 34, 34, -52, 50, 94, -60, 64, 58],22,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],33,),
    ([48, 2, 79, 98, 28, 17, 41, 47, 61, 76, 82, 5, 74, 4, 80, 51, 22, 45, 91, 75, 91, 93, 42, 45, 69, 98, 76, 74, 83, 17, 30, 88, 53, 25, 35, 19, 26],20,),
    ([-88, -84, -82, -74, -44, -34, -32, -20, -20, -14, 6, 6, 10, 12, 16, 24, 32, 34, 38, 46, 54, 54, 56, 60, 82, 88, 90, 94, 98],24,),
    ([0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],7,),
    ([10, 14, 14, 14, 19, 20, 22, 26, 35, 36, 40, 53, 54, 55, 55, 57, 57, 67, 72, 72, 77, 78, 83, 84, 95, 96],16,),
    ([-80, 18, -76, 48, -52, -38, 52, -82, 40, -44, -90, 86, -86, -36, -32, -2, 56, -12, -88, 14, -16, 8, 52, 24, 46, 56, 84, -36, 84, -60, 72, -46, 32, -16, -20, 68, -86, -62, 58, 8, 78, -52, 22, -28, -22, -42, 12, -48],30,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],14,),
    ([20, 94, 36, 2, 50, 62, 84, 50, 66, 75, 1, 18, 41, 48, 72, 61, 86, 22, 54, 6, 71, 46, 92, 68, 59, 51, 89, 31, 58, 78, 82, 84],25,)
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
