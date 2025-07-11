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
    found = False
    arr.sort ( )
    for i in range ( 0 , n - 1 ) :
        l = i + 1
        r = n - 1
        x = arr [ i ]
        while ( l < r ) :
            if ( x + arr [ l ] + arr [ r ] == 0 ) :
                print ( x , arr [ l ] , arr [ r ] )
                l += 1
                r -= 1
                found = True
            elif ( x + arr [ l ] + arr [ r ] < 0 ) :
                l += 1
            else :
                r -= 1
    if ( found == False ) :
        print ( " No Triplet Found" )


def f_filled ( arr , n ) :
    found = False
    arr.sort ( )
    for i in range ( n - 1 ) :
        l = i + 1
        r = n - 1
        x = arr [ i ]
        while l < r :
            if x + arr [ l ] + arr [ r ] == 0 :
                print ( x , end = ' ' )
                print ( arr [ l ] , end = ' ' )
                print ( arr [ r ] , end = ' ' )
                l += 1
                r -= 1
                found = True
            elif x + arr [ l ] + arr [ r ] < 0 :
                l += 1
            else :
                r -= 1
    if found == False :
        print ( ' No Triplet Found' )

if __name__ == '__main__':
    param = [
    ([4, 24, 27, 34, 39, 41, 67, 69, 84, 91, 94],7,),
    ([14, 8, 92, 46, 62, 8, 8, 70, 98, -20, -16, -6, -2, -36, 46, 46, -26, 50, 76, 96, -32, 2, -32, 72, 48, 24, 64, 42, 40, 92],29,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],15,),
    ([47, 69, 42, 36, 82, 65, 84],3,),
    ([-98, -74, -62, -60, -60, -32],5,),
    ([1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0],35,),
    ([1, 4, 4, 9, 20, 23, 24, 27, 28, 29, 31, 35, 42, 45, 46, 47, 49, 52, 55, 57, 62, 67, 72, 78, 79, 82, 86, 86, 88],26,),
    ([92, 0, 56, 90, -10, -46, 44, -86, -16, -90, -92, -44, -88, 24, -80, -98, 68, -86, 98, -10, 18, -40, 98, 40, -58, -6, -38, 72, 90],15,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],17,),
    ([7, 3, 37, 60, 6, 26, 30, 21, 7, 59, 18, 69, 40, 47, 34, 19, 51, 27, 4, 7, 56, 4, 57, 62, 54, 9, 93, 31, 9, 85],28,)
        ]
    filled_function_param = [
    ([4, 24, 27, 34, 39, 41, 67, 69, 84, 91, 94],7,),
    ([14, 8, 92, 46, 62, 8, 8, 70, 98, -20, -16, -6, -2, -36, 46, 46, -26, 50, 76, 96, -32, 2, -32, 72, 48, 24, 64, 42, 40, 92],29,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],15,),
    ([47, 69, 42, 36, 82, 65, 84],3,),
    ([-98, -74, -62, -60, -60, -32],5,),
    ([1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0],35,),
    ([1, 4, 4, 9, 20, 23, 24, 27, 28, 29, 31, 35, 42, 45, 46, 47, 49, 52, 55, 57, 62, 67, 72, 78, 79, 82, 86, 86, 88],26,),
    ([92, 0, 56, 90, -10, -46, 44, -86, -16, -90, -92, -44, -88, 24, -80, -98, 68, -86, 98, -10, 18, -40, 98, 40, -58, -6, -38, 72, 90],15,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],17,),
    ([7, 3, 37, 60, 6, 26, 30, 21, 7, 59, 18, 69, 40, 47, 34, 19, 51, 27, 4, 7, 56, 4, 57, 62, 54, 9, 93, 31, 9, 85],28,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        f_filled(*(filled_function_param[i]))
        f_gold(*parameters_set)
        if parameters_set == filled_function_param[i]:
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))