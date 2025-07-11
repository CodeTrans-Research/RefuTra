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
def f_gold ( arr , n ) :
    for i in range ( 0 , n ) :
        if ( arr [ i ] & 1 ) :
            arr [ i ] *= - 1
    arr.sort ( )
    for i in range ( 0 , n ) :
        if ( arr [ i ] & 1 ) :
            arr [ i ] *= - 1


def f_filled ( arr , n ) :
    for i in range ( n ) :
        if ( arr [ i ] & 1 ) :
            arr [ i ] *= - 1
    arr.sort ( )
    for i in range ( n ) :
        if ( arr [ i ] & 1 ) :
            arr [ i ] *= - 1

if __name__ == '__main__':
    param = [
    ([4],0,),
    ([8, -74, 89, 65, 51, -15, 68, 51, 23, 44, 89],8,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],28,),
    ([51, 74, 43, 15, 38, 15, 5, 93],6,),
    ([-96, -75, -64, -20, -5, -2, 1, 40, 46, 64],7,),
    ([0, 0, 1, 0, 0, 1, 0, 0, 0],5,),
    ([1, 2, 4, 4, 17, 22, 23, 28, 35, 38, 39, 39, 41, 42, 42, 45, 46, 49, 49, 49, 50, 59, 62, 68, 69, 71, 73, 76, 78, 79, 80, 87, 88, 88, 90, 90, 91, 93, 95, 96, 98],34,),
    ([11, 68, -52, -49, -57, -2, 83, 77, 24, -20, 85, 11, 43, -73, 96, 92, 58, 64, 95, 13, -14, 14, 24, -51, -24, -45, -44, 96, -5, -56, 59],24,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],14,),
    ([44, 7, 44, 68, 34, 66, 69, 55, 10, 96, 42, 41, 77, 69, 10, 10, 91, 60, 51],13,)
        ]
    filled_function_param = [
    ([4],0,),
    ([8, -74, 89, 65, 51, -15, 68, 51, 23, 44, 89],8,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],28,),
    ([51, 74, 43, 15, 38, 15, 5, 93],6,),
    ([-96, -75, -64, -20, -5, -2, 1, 40, 46, 64],7,),
    ([0, 0, 1, 0, 0, 1, 0, 0, 0],5,),
    ([1, 2, 4, 4, 17, 22, 23, 28, 35, 38, 39, 39, 41, 42, 42, 45, 46, 49, 49, 49, 50, 59, 62, 68, 69, 71, 73, 76, 78, 79, 80, 87, 88, 88, 90, 90, 91, 93, 95, 96, 98],34,),
    ([11, 68, -52, -49, -57, -2, 83, 77, 24, -20, 85, 11, 43, -73, 96, 92, 58, 64, 95, 13, -14, 14, 24, -51, -24, -45, -44, 96, -5, -56, 59],24,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],14,),
    ([44, 7, 44, 68, 34, 66, 69, 55, 10, 96, 42, 41, 77, 69, 10, 10, 91, 60, 51],13,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        f_filled(*(filled_function_param[i]))
        f_gold(*parameters_set)
        if parameters_set == filled_function_param[i]:
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))