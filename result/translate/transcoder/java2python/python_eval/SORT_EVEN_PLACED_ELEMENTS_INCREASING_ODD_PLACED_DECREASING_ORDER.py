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
    evenArr = [ ]
    oddArr = [ ]
    for i in range ( n ) :
        if ( ( i % 2 ) == 0 ) :
            evenArr.append ( arr [ i ] )
        else :
            oddArr.append ( arr [ i ] )
    evenArr = sorted ( evenArr )
    oddArr = sorted ( oddArr )
    oddArr = oddArr [ : : - 1 ]
    i = 0
    for j in range ( len ( evenArr ) ) :
        arr [ i ] = evenArr [ j ]
        i += 1
    for j in range ( len ( oddArr ) ) :
        arr [ i ] = oddArr [ j ]
        i += 1


def f_filled ( arr , n ) :
    evenArr = [ ]
    oddArr = [ ]
    for i in range ( n ) :
        if i % 2 != 1 :
            evenArr.append ( arr [ i ] )
        else :
            oddArr.append ( arr [ i ] )
    evenArr.sort ( )
    oddArr.sort ( )
    i = 0
    for j in evenArr :
        arr [ i ] = evenArr [ j ]
    for j in oddArr :
        arr [ i ] = oddArr [ j ]
    return arr

if __name__ == '__main__':
    param = [
    ([6, 6, 6, 10, 15, 21, 38, 50, 51, 72, 79, 81, 82, 84, 85, 86, 87],15,),
    ([82, -36, 18, -88, -24, 20, 26, -52, 28, 2],7,),
    ([0, 0, 0, 1, 1, 1],3,),
    ([81, 47, 38, 70, 35, 43, 94, 30, 57, 55, 78, 97, 72, 1],8,),
    ([-80, -78, -72, -46, -26, -24, -20, 8, 16, 26, 38, 44, 54, 68, 68, 78, 86, 92],11,),
    ([0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0],21,),
    ([3, 4, 9, 12, 20, 30, 33, 34, 37, 38, 50, 51, 52, 54, 60, 69, 73, 74, 92, 93, 94, 97, 98],13,),
    ([86, -32, 64, -36, -36, -30, -66, -60, -76, -56, -60, -16, -60, -98, -18, 72, -14],10,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],29,),
    ([61, 11, 46, 40, 82, 35, 37, 41, 52, 76, 13, 53, 53, 3, 40, 29, 7, 51, 20, 51, 87, 1, 80, 73, 89, 93, 1, 71, 33, 50, 62, 85, 46, 1, 71, 54, 81, 85],36,)
        ]
    filled_function_param = [
    ([6, 6, 6, 10, 15, 21, 38, 50, 51, 72, 79, 81, 82, 84, 85, 86, 87],15,),
    ([82, -36, 18, -88, -24, 20, 26, -52, 28, 2],7,),
    ([0, 0, 0, 1, 1, 1],3,),
    ([81, 47, 38, 70, 35, 43, 94, 30, 57, 55, 78, 97, 72, 1],8,),
    ([-80, -78, -72, -46, -26, -24, -20, 8, 16, 26, 38, 44, 54, 68, 68, 78, 86, 92],11,),
    ([0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0],21,),
    ([3, 4, 9, 12, 20, 30, 33, 34, 37, 38, 50, 51, 52, 54, 60, 69, 73, 74, 92, 93, 94, 97, 98],13,),
    ([86, -32, 64, -36, -36, -30, -66, -60, -76, -56, -60, -16, -60, -98, -18, 72, -14],10,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],29,),
    ([61, 11, 46, 40, 82, 35, 37, 41, 52, 76, 13, 53, 53, 3, 40, 29, 7, 51, 20, 51, 87, 1, 80, 73, 89, 93, 1, 71, 33, 50, 62, 85, 46, 1, 71, 54, 81, 85],36,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        f_filled(*(filled_function_param[i]))
        f_gold(*parameters_set)
        if parameters_set == filled_function_param[i]:
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))