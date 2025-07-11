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
def f_gold ( arr , n , k ) :
    for i in range ( 0 , k ) :
        x = arr [ 0 ]
        for j in range ( 0 , n - 1 ) :
            arr [ j ] = arr [ j + 1 ]
        arr [ n - 1 ] = x


def f_filled(arr, n, k):
    for i in range(k):
        x = arr[0]
        for j in range(n - 1):
            arr[j] = arr[j + 1]
        arr[n - 1] = x

if __name__ == '__main__':
    param = [
    ([75],0,0,),
    ([-58, -60, -38, 48, -2, 32, -48, -46, 90, -54, -18, 28, 72, 86, 0, -2, -74, 12, -58, 90, -30, 10, -88, 2, -14, 82, -82, -46, 2, -74],27,17,),
    ([0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],7,7,),
    ([45, 51, 26, 36, 10, 62, 62, 56, 61, 67, 86, 97, 31, 93, 32, 1, 14, 25, 24, 30, 1, 44, 7, 98, 56, 68, 53, 59, 30, 90, 79, 22],23,24,),
    ([-88, -72, -64, -46, -40, -16, -8, 0, 22, 34, 44],6,6,),
    ([0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0],23,30,),
    ([8, 17, 20, 23, 31, 32, 37, 37, 44, 45, 48, 64, 64, 67, 69, 71, 75, 77, 78, 81, 83, 87, 89, 92, 94],21,20,),
    ([-8, -88, -68, 48, 8, 50, 30, -88, 74, -16, 6, 74, 36, 32, 22, 96, -2, 70, 40, -46, 98, 34, 2, 94],23,13,),
    ([0, 0, 0, 0, 1, 1, 1, 1, 1],5,8,),
    ([80, 14, 35, 25, 60, 86, 45, 95, 32, 29, 94, 6, 63, 66, 38],9,7,)
        ]
    filled_function_param = [
    ([75],0,0,),
    ([-58, -60, -38, 48, -2, 32, -48, -46, 90, -54, -18, 28, 72, 86, 0, -2, -74, 12, -58, 90, -30, 10, -88, 2, -14, 82, -82, -46, 2, -74],27,17,),
    ([0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],7,7,),
    ([45, 51, 26, 36, 10, 62, 62, 56, 61, 67, 86, 97, 31, 93, 32, 1, 14, 25, 24, 30, 1, 44, 7, 98, 56, 68, 53, 59, 30, 90, 79, 22],23,24,),
    ([-88, -72, -64, -46, -40, -16, -8, 0, 22, 34, 44],6,6,),
    ([0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0],23,30,),
    ([8, 17, 20, 23, 31, 32, 37, 37, 44, 45, 48, 64, 64, 67, 69, 71, 75, 77, 78, 81, 83, 87, 89, 92, 94],21,20,),
    ([-8, -88, -68, 48, 8, 50, 30, -88, 74, -16, 6, 74, 36, 32, 22, 96, -2, 70, 40, -46, 98, 34, 2, 94],23,13,),
    ([0, 0, 0, 0, 1, 1, 1, 1, 1],5,8,),
    ([80, 14, 35, 25, 60, 86, 45, 95, 32, 29, 94, 6, 63, 66, 38],9,7,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        f_filled(*(filled_function_param[i]))
        f_gold(*parameters_set)
        if parameters_set == filled_function_param[i]:
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))