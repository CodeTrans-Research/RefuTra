import sys
import math
import heapq
from queue import Queue# Copyright (c) 2019-present, Facebook, Inc.
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
    second = - sys.maxsize
    third = - sys.maxsize
    for i in range ( 1 , arr_size ) :
        if ( arr [ i ] > first ) :
            third = second
            second = first
            first = arr [ i ]
        elif ( arr [ i ] > second ) :
            third = second
            second = arr [ i ]
        elif ( arr [ i ] > third ) :
            third = arr [ i ]
    print ( "The third Largest" , "element is" , third )


def f_filled(arr, arr_size):
        if arr_size < 3:
            print("Invalid Input")
            return
        first = arr[0]
        second = float("-inf")
        third = float("-inf")
        for i in range(1, arr_size):
            if arr[i] > first:
                third, second = second, first
                first = arr[i]
            elif arr[i] > second:
                third = second
                second = arr[i]
            elif arr[i] > third:
                third = arr[i]
        print("The third Largest element is", third)

if __name__ == '__main__':
    param = [
    ([1, 1, 2, 4, 9, 9, 11, 14, 19, 26, 28, 32, 33, 34, 37, 41, 42, 42, 48, 49, 49, 52, 59, 61, 63, 66, 71, 71, 74, 76, 78, 80, 80, 87, 87, 88, 92, 96, 97],19,),
    ([28, -24, 54, 14, -16, -88, -74, -80, 66, -80, 64, 36, -24, 40, -54, 10, 86, -24, -68, -12, 58, -90, 30, 16, 6],14,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],25,),
    ([7, 19, 58, 93, 76, 88, 89, 63],7,),
    ([-98, -92, -86, -84, -70, -66, -62, -60, -54, -52, -50, -48, -40, -38, -36, -36, -36, -36, -32, -32, -30, -22, -14, -8, 0, 0, 4, 4, 12, 14, 26, 34, 38, 46, 46, 46, 46, 48, 52, 64, 68, 76, 76, 82, 84, 88, 88, 88, 96],35,),
    ([0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],23,),
    ([32, 63, 82, 94],2,),
    ([-34, -32, 20, -54, -84, 64, -86, -82, -4, 32, 20, 20, -4, 74, 36, 38, -54, -58, -48, 84, 86, -82, -44, -48, -16, -50, -50, -74],27,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],29,),
    ([82, 3, 98, 95, 22, 77, 44, 69, 13, 34, 91, 33, 82, 60, 81, 13, 7, 93, 73, 73, 66, 67, 49, 91, 88, 13, 76, 8],25,)
        ]
    filled_function_param = [
    ([1, 1, 2, 4, 9, 9, 11, 14, 19, 26, 28, 32, 33, 34, 37, 41, 42, 42, 48, 49, 49, 52, 59, 61, 63, 66, 71, 71, 74, 76, 78, 80, 80, 87, 87, 88, 92, 96, 97],19,),
    ([28, -24, 54, 14, -16, -88, -74, -80, 66, -80, 64, 36, -24, 40, -54, 10, 86, -24, -68, -12, 58, -90, 30, 16, 6],14,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],25,),
    ([7, 19, 58, 93, 76, 88, 89, 63],7,),
    ([-98, -92, -86, -84, -70, -66, -62, -60, -54, -52, -50, -48, -40, -38, -36, -36, -36, -36, -32, -32, -30, -22, -14, -8, 0, 0, 4, 4, 12, 14, 26, 34, 38, 46, 46, 46, 46, 48, 52, 64, 68, 76, 76, 82, 84, 88, 88, 88, 96],35,),
    ([0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],23,),
    ([32, 63, 82, 94],2,),
    ([-34, -32, 20, -54, -84, 64, -86, -82, -4, 32, 20, 20, -4, 74, 36, 38, -54, -58, -48, 84, 86, -82, -44, -48, -16, -50, -50, -74],27,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],29,),
    ([82, 3, 98, 95, 22, 77, 44, 69, 13, 34, 91, 33, 82, 60, 81, 13, 7, 93, 73, 73, 66, 67, 49, 91, 88, 13, 76, 8],25,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        f_filled(*(filled_function_param[i]))
        f_gold(*parameters_set)
        if parameters_set == filled_function_param[i]:
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))