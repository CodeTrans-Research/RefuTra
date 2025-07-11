import sys
import math
import heapq
from queue import Queue# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( arr , arr_size ) :
    for i in range ( 0 , arr_size ) :
        count = 0
        for j in range ( 0 , arr_size ) :
            if arr [ i ] == arr [ j ] :
                count += 1
        if ( count % 2 != 0 ) :
            return arr [ i ]
    return - 1


def f_filled(arr, arr_size):
        for i in range(arr_size):
            count = 0
            for j in range(arr_size):
                if arr[i] == arr[j]:
                    count += 1
            if count % 2!= 0:
                return arr[i]
        return -1

if __name__ == '__main__':
    param = [
    ([1, 5, 5, 8, 14, 15, 17, 17, 18, 23, 23, 25, 26, 35, 36, 39, 51, 53, 56, 56, 60, 62, 64, 64, 65, 66, 67, 68, 71, 75, 80, 82, 83, 88, 89, 91, 91, 92, 93, 95, 99],31,),
    ([-56, 98, 44, 30, -88, 18, 60, 86, 4, 16, 10, 64, -22, -86, -66, -16, 70, -44, 98, 78, -96, -66, 92, 10, 40, -16],19,),
    ([0, 0, 0, 0, 0, 1, 1, 1],6,),
    ([36, 11, 83, 41, 42, 14, 46, 89, 91, 96, 57, 42, 74, 73, 9, 26, 79, 40, 31, 69, 44, 39, 14, 92, 34, 20, 52, 47, 14],25,),
    ([-84, -84, -84, -78, -66, -62, -62, -36, -24, -10, -10, -8, -4, -2, 12, 14, 20, 22, 36, 42, 46, 66, 84, 96, 96, 98],23,),
    ([1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],19,),
    ([11, 12, 14, 28, 42, 48, 50, 58, 67, 74, 86, 89, 95],7,),
    ([52, -56, -6, 74, 10, 68, 74, 10, 16, -80, 82, -32, 6, -6, 82, 20],11,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],31,),
    ([4, 80, 92],1,)
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
