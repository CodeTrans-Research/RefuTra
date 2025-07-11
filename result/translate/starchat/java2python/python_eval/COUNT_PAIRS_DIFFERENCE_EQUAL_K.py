import sys
import math
import heapq
from queue import Queue# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( arr , n , k ) :
    count = 0
    for i in range ( 0 , n ) :
        for j in range ( i + 1 , n ) :
            if arr [ i ] - arr [ j ] == k or arr [ j ] - arr [ i ] == k :
                count += 1
    return count


def f_filled(arr, n, k):
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                if (arr[i] - arr[j] == k or arr[j] - arr[i] == k):
                    count += 1
        return count

if __name__ == '__main__':
    param = [
    ([9, 14, 17, 19, 22, 23, 23, 27, 30, 31, 34, 37, 37, 39, 39, 42, 57, 61, 68, 73, 77, 79, 91, 96, 97],19,19,),
    ([-78, -42, 28, -88, 18, -52],3,4,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],16,14,),
    ([8, 46, 57, 28, 80, 2, 75, 57, 83, 45, 32, 49, 77, 30, 94, 33, 23, 29, 35, 81, 85],15,11,),
    ([-90, -72, -72, -62, -62, -54, -54, -52, -48, -38, -22, -22, -22, -12, -12, -8, -8, -8, -6, -6, -2, 6, 12, 26, 26, 28, 28, 38, 40, 48, 52, 52, 58, 60, 68, 70, 72, 76, 76, 76, 92],22,25,),
    ([0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1],45,39,),
    ([3, 13, 19, 23, 27, 32, 49, 52, 54, 57, 58, 58, 63, 67, 68, 68, 69, 70, 75, 80, 86, 90, 91, 95],19,21,),
    ([-56, 40, -66, 42, 8, -40, -8, -42],7,6,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],16,28,),
    ([99, 12, 90, 10, 86, 86, 81, 19, 1, 1, 98, 82, 34, 39, 34, 1, 54, 47, 39, 82, 21, 50, 82, 41, 98, 47, 88, 46, 72, 28, 28, 29, 60, 87, 92, 53, 93, 29, 74, 75, 11, 32, 48, 47, 85, 16, 20],24,45,)
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
