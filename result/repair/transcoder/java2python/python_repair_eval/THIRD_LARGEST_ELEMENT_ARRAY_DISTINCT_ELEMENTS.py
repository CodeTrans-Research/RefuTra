import sys
import math
import heapq
from queue import Queue
import numpy as np
# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
import sys

def f_gold ( arr , arr_size ) :
    if ( arr_size < 3 ) :
        print ( " Invalid Input " )
        return
    first = arr [ 0 ]
    for i in range ( 1 , arr_size ) :
        if ( arr [ i ] > first ) :
            first = arr [ i ]
    second = - sys.maxsize
    for i in range ( 0 , arr_size ) :
        if ( arr [ i ] > second and arr [ i ] < first ) :
            second = arr [ i ]
    third = - sys.maxsize
    for i in range ( 0 , arr_size ) :
        if ( arr [ i ] > third and arr [ i ] < second ) :
            third = arr [ i ]
    print ( "The Third Largest" , "element is" , third )


def f_filled ( arr , arr_size ) :
    if arr_size < 3 :
        print ( " Invalid Input " )
        return
    first = arr [ 0 ]
    for i in range ( 1 , arr_size ) :
        if arr [ i ] > first :
            first = arr [ i ]
    second = -sys.maxsize
    for i in range ( arr_size ) :
        if arr [ i ] > second and arr [ i ] < first :
            second = arr [ i ]
    third = -sys.maxsize
    for i in range ( arr_size ) :
        if arr [ i ] > third and arr [ i ] < second :
            third = arr [ i ]
    print ( "The third Largest " "element is " , third )

if __name__ == '__main__':
    param = [
    ([10, 17, 28, 42, 42, 45, 49, 54, 55, 58, 80, 82, 88, 91],12,),
    ([-34, 10, 52, -38, 58, -14, -26, 96, 22, 74, -28, 20, 78, 94, -38, -26, 58, 10, -56, 10, 50, 66, -60, -96, 74],12,),
    ([0, 0, 0, 0, 0, 0, 1, 1],6,),
    ([33, 24, 18, 31, 49, 18, 70, 64, 66, 13, 65, 62, 6, 39, 77, 59, 28, 63, 32, 88, 59, 84, 20, 2, 42, 29, 99, 40, 9, 41, 47, 46],25,),
    ([40],0,),
    ([0, 1, 0, 0],2,),
    ([7, 7, 10, 12, 20, 21, 27, 32, 37, 40, 43, 44, 44, 45, 47, 47, 50, 53, 56, 60, 68, 70, 81, 89, 92, 95, 95],26,),
    ([94, -96, 52, -78, -52, -14, 78, 66, 74, -80, 82, 90, -40, -84, 44, -72, -18, -98, 84, -22, 32, 18, -72, 94, -10, 84, 52, 2, -48, 80, -68, 64, -80, -92, -18, -50, 88, -98, -98, -50, 60, -20, -38, 12, -54, 30, -54, -32, -42],43,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],24,),
    ([43, 88, 28, 24, 58, 40, 33, 90, 69, 37, 13, 9, 28, 83, 65, 63, 96, 36, 64, 20, 21, 90, 60, 18, 58, 18, 68, 58, 50, 13, 79, 92, 3, 63, 19, 20, 79, 68, 83, 47],24,)
        ]
    filled_function_param = [
    ([10, 17, 28, 42, 42, 45, 49, 54, 55, 58, 80, 82, 88, 91],12,),
    ([-34, 10, 52, -38, 58, -14, -26, 96, 22, 74, -28, 20, 78, 94, -38, -26, 58, 10, -56, 10, 50, 66, -60, -96, 74],12,),
    ([0, 0, 0, 0, 0, 0, 1, 1],6,),
    ([33, 24, 18, 31, 49, 18, 70, 64, 66, 13, 65, 62, 6, 39, 77, 59, 28, 63, 32, 88, 59, 84, 20, 2, 42, 29, 99, 40, 9, 41, 47, 46],25,),
    ([40],0,),
    ([0, 1, 0, 0],2,),
    ([7, 7, 10, 12, 20, 21, 27, 32, 37, 40, 43, 44, 44, 45, 47, 47, 50, 53, 56, 60, 68, 70, 81, 89, 92, 95, 95],26,),
    ([94, -96, 52, -78, -52, -14, 78, 66, 74, -80, 82, 90, -40, -84, 44, -72, -18, -98, 84, -22, 32, 18, -72, 94, -10, 84, 52, 2, -48, 80, -68, 64, -80, -92, -18, -50, 88, -98, -98, -50, 60, -20, -38, 12, -54, 30, -54, -32, -42],43,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],24,),
    ([43, 88, 28, 24, 58, 40, 33, 90, 69, 37, 13, 9, 28, 83, 65, 63, 96, 36, 64, 20, 21, 90, 60, 18, 58, 18, 68, 58, 50, 13, 79, 92, 3, 63, 19, 20, 79, 68, 83, 47],24,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        f_filled(*(filled_function_param[i]))
        f_gold(*parameters_set)
        if parameters_set == filled_function_param[i]:
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))