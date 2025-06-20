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
    arr.sort ( )
    a = 0 ; b = 0
    for i in range ( n ) :
        if ( i % 2 != 0 ) :
            a = a * 10 + arr [ i ]
        else :
            b = b * 10 + arr [ i ]
    return a + b


def f_filled(arr, n):
        arr.sort()
        a = 0
        b = 0
        for i in range(n):
            if i % 2!= 0:
                a = a * 10 + arr[i]
            else:
                b = b * 10 + arr[i]
        return a + b

if __name__ == '__main__':
    param = [
    ([3, 4, 5, 10, 14, 16, 18, 42, 43, 43, 45, 46, 51, 52, 53, 58, 61, 66, 79, 81, 82, 84],19,),
    ([48, -22, 60, 32, 48, -2, -76, -50, -26, 56, -86, 98, -30, -22, 82, -20, 58, 40, 76, -2, 82, -90, 8, -46, 22, 94],25,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],23,),
    ([79, 45],1,),
    ([-90, -68, -38, -34, -4, 6, 10, 28, 48, 52, 54, 68, 88, 90],11,),
    ([1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0],22,),
    ([4, 8, 8, 23, 26, 27, 30, 42, 44, 55, 59, 64, 67, 69, 74, 77, 82, 82, 87, 96, 97],17,),
    ([0, -18, -98, -36, -62, 0, -32, -98, 46, 72, -18, 30, -86, -42, -82, 2, -76, -64, -66, -48, -28, 52, -46, -76, 76, 10, 70, 4, 18, 94, 88, 80, -60, -36, 62, 96, -4, 88, 50],32,),
    ([0, 0, 0, 0, 0, 0, 1, 1, 1, 1],6,),
    ([8, 71, 75, 58, 97, 24, 56, 98, 71, 69, 32, 64, 54, 96, 69, 22, 7, 47, 45, 68, 17, 36, 90, 9, 71, 86, 16, 61, 53, 63, 9, 74, 38, 87, 14, 86, 42, 42, 14, 43, 58, 82, 72, 73, 32],25,)
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
