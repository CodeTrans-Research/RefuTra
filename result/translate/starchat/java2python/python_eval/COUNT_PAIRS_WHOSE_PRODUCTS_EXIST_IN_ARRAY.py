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
    result = 0 ;
    for i in range ( 0 , n ) :
        for j in range ( i + 1 , n ) :
            product = arr [ i ] * arr [ j ] ;
            for k in range ( 0 , n ) :
                if ( arr [ k ] == product ) :
                    result = result + 1 ;
                    break ;
    return result ;


def f_filled(arr, n):
        result = 0
        for i in range(n):
            for j in range(i + 1, n):
                product = arr[i] * arr[j]
                for k in range(n):
                    if arr[k] == product:
                        result += 1
                        break
        return result

if __name__ == '__main__':
    param = [
    ([3, 7, 26, 40, 46, 89, 99],5,),
    ([98, 42, -24, -60, 74, 86, 6, 8, 72, -58, 38, -20, 6, -6, 8, 48, -34, 30, 60, 66, 38, -54, 8, -94, -8, 0, -64, -94, -94, -72, -84, -36, 88, -62, -88, 46, -4, 88],24,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],44,),
    ([37, 97, 57, 82, 29, 68, 94, 38, 81, 48, 13, 84, 57, 5, 27, 87, 11, 35, 82, 53, 67, 31, 15, 99, 6, 93, 91, 92, 3, 23, 90, 27, 6, 33, 78, 3, 19, 19, 27],36,),
    ([-80, -74, -72, -72, -66, -66, -62, -50, -44, -44, -28, -24, -24, -22, -16, -10, -6, -4, -2, 2, 2, 4, 12, 16, 16, 28, 30, 32, 32, 38, 38, 72, 84, 86, 88, 90, 96],34,),
    ([0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1],18,),
    ([25, 67],1,),
    ([82, 74, -82, 22, -28, -78, -22, -86, -74, 42, -6, 54, -88, -92, -14, -50, 68, 46, -50, 46, -18, 66, -76, -30, 36, 12, 66],14,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],32,),
    ([50, 23, 56, 9],3,)
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
