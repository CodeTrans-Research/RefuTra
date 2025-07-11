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
    max_idx = n - 1
    min_idx = 0
    max_elem = arr [ n - 1 ] + 1
    for i in range ( 0 , n ) :
        if i % 2 == 0 :
            arr [ i ] += ( arr [ max_idx ] % max_elem ) * max_elem
            max_idx -= 1
        else :
            arr [ i ] += ( arr [ min_idx ] % max_elem ) * max_elem
            min_idx += 1
    for i in range ( 0 , n ) :
        arr [ i ] = arr [ i ] // max_elem


def f_filled(arr, n):
        max_elem = arr[n - 1] + 1
        for i in range(n):
            if i % 2 == 0:
                arr[i] += (arr[max_idx] % max_elem) * max_elem
                max_idx -= 1
            else:
                arr[i] += (arr[min_idx] % max_elem) * max_elem
                min_idx += 1
        for i in range(n):
            arr[i] = arr[i] // max_elem

if __name__ == '__main__':
    param = [
    ([1, 1, 2, 3, 9, 10, 14, 22, 26, 28, 29, 29, 30, 32, 32, 32, 34, 37, 39, 40, 42, 42, 42, 43, 45, 47, 49, 52, 53, 54, 56, 58, 59, 68, 71, 73, 76, 81, 81, 83, 84, 91, 94],29,),
    ([50, 46, 6, -57, 67, 34, -52, 26, -93, 97, -84, 29, 15, -63, 65, 25, -19, 92, -38, -28, 89, 25, 61, -34, -70, -80, 88, -18, 7, 52, 32, -63, 32, -23, -11, 46, -12, 94, 76, -67, -42],38,),
    ([0, 0, 0, 0, 0, 0, 1, 1, 1],4,),
    ([15, 99, 57, 69, 22, 64, 41, 87, 71, 56, 23, 25, 91, 6, 34, 63, 9, 60, 49, 97, 51, 60, 70, 37, 31, 98, 41, 62, 93, 58, 14, 36, 36, 79, 8, 26, 36, 48, 85, 28, 68, 62, 80, 86, 76, 80, 51],30,),
    ([-99, -99, -90, -90, -85, -85, -79, -77, -72, -71, -67, -66, -61, -39, -39, -35, -35, -23, -20, -18, -16, -13, -2, 1, 5, 6, 10, 24, 27, 32, 33, 38, 48, 67, 70, 76, 82, 88],34,),
    ([0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0],33,),
    ([2, 22, 32, 34, 43, 66, 70, 74, 94, 94],6,),
    ([-99, -28, 76, -50, 41, -85, -47, 72, -92, -26, -54, -31, 14, 47, 66, 23],10,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],42,),
    ([19, 31, 26, 42, 41, 23, 47, 13, 89, 66, 66, 16, 73, 28, 77, 35, 41, 77, 31, 85, 32, 54, 98, 72, 59],20,)
        ]
    filled_function_param = [
    ([1, 1, 2, 3, 9, 10, 14, 22, 26, 28, 29, 29, 30, 32, 32, 32, 34, 37, 39, 40, 42, 42, 42, 43, 45, 47, 49, 52, 53, 54, 56, 58, 59, 68, 71, 73, 76, 81, 81, 83, 84, 91, 94],29,),
    ([50, 46, 6, -57, 67, 34, -52, 26, -93, 97, -84, 29, 15, -63, 65, 25, -19, 92, -38, -28, 89, 25, 61, -34, -70, -80, 88, -18, 7, 52, 32, -63, 32, -23, -11, 46, -12, 94, 76, -67, -42],38,),
    ([0, 0, 0, 0, 0, 0, 1, 1, 1],4,),
    ([15, 99, 57, 69, 22, 64, 41, 87, 71, 56, 23, 25, 91, 6, 34, 63, 9, 60, 49, 97, 51, 60, 70, 37, 31, 98, 41, 62, 93, 58, 14, 36, 36, 79, 8, 26, 36, 48, 85, 28, 68, 62, 80, 86, 76, 80, 51],30,),
    ([-99, -99, -90, -90, -85, -85, -79, -77, -72, -71, -67, -66, -61, -39, -39, -35, -35, -23, -20, -18, -16, -13, -2, 1, 5, 6, 10, 24, 27, 32, 33, 38, 48, 67, 70, 76, 82, 88],34,),
    ([0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0],33,),
    ([2, 22, 32, 34, 43, 66, 70, 74, 94, 94],6,),
    ([-99, -28, 76, -50, 41, -85, -47, 72, -92, -26, -54, -31, 14, 47, 66, 23],10,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],42,),
    ([19, 31, 26, 42, 41, 23, 47, 13, 89, 66, 66, 16, 73, 28, 77, 35, 41, 77, 31, 85, 32, 54, 98, 72, 59],20,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        f_filled(*(filled_function_param[i]))
        f_gold(*parameters_set)
        if parameters_set == filled_function_param[i]:
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))
