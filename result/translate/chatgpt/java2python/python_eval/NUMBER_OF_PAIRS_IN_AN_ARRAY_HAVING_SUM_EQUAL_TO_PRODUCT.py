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
def f_gold ( a , n ) :
    zero = 0
    two = 0
    for i in range ( n ) :
        if a [ i ] == 0 :
            zero += 1
        if a [ i ] == 2 :
            two += 1
    cnt = ( zero * ( zero - 1 ) ) // 2 + \
        ( two * ( two - 1 ) ) // 2
    return cnt


def f_filled(a, n):
    zero = 0
    two = 0
    for i in range(n):
        if a[i] == 0:
            zero += 1
        if a[i] == 2:
            two += 1
    cnt = (zero * (zero - 1)) // 2 + (two * (two - 1)) // 2
    return cnt

if __name__ == '__main__':
    param = [
    ([9, 10, 20, 26, 26, 28, 31, 34, 35, 36, 36, 37, 39, 43, 44, 44, 46, 49, 54, 57, 58, 63, 64, 64, 65, 67, 70, 70, 74, 75, 77, 78, 79, 81, 82, 83, 84, 86, 95],31,),
    ([0, -10, 10, 0, 68, 4, -6, -14, 74, -80, 56, -4, 36, 56, 10, -16, 90, 84, -38, -40, 40, -86, -36, -16, -48, -76, -72, -18, -14, -40, -82, 56, -60],19,),
    ([0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],22,),
    ([88, 20, 53, 21, 29, 73, 62, 91, 72, 34, 47, 42, 98, 9, 79, 80, 94, 36, 7, 67, 96, 34, 99, 56, 37, 70, 55, 36, 10, 77, 41, 51, 5, 37, 57, 29, 56, 74, 97, 31, 96, 52, 13, 29, 87, 58, 28, 31],38,),
    ([20],0,),
    ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1],21,),
    ([2, 4, 9, 16, 22, 23, 25, 33, 33, 36, 39, 48, 49, 52, 53, 60, 67, 68, 76, 77, 79, 84, 84, 86, 89],24,),
    ([-62, 42, -88, -44, 90, 30, 52, 54, 56, -72, -76, 90, 18, 42, 62, -84, 56, -80, 72],13,),
    ([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],15,),
    ([22, 15, 28, 29, 32, 16, 33, 83],7,)
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
