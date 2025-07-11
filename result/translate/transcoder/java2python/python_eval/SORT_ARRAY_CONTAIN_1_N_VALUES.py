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
    for i in range ( n ) :
        arr [ i ] = i + 1


def f_filled ( arr , n ) :
    for i in range ( n ) :
        arr [ i ] = i + 1

if __name__ == '__main__':
    param = [
    ([3, 3, 6, 7, 9, 11, 15, 15, 17, 19, 21, 23, 26, 27, 37, 48, 48, 51, 53, 53, 59, 64, 69, 69, 70, 71, 72, 84, 93, 96],19,),
    ([66, -28, 6, 25, -65, 19, -86, -86, -90, 40, -62],8,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],26,),
    ([85, 84, 8, 36, 93, 76, 14, 54, 85, 86],9,),
    ([-90, -82, -80, -73, -67, -62, -62, -61, -58, -56, -56, -52, -50, -49, -49, -43, -43, -30, -26, -26, -15, -14, -13, -4, 10, 19, 20, 22, 26, 29, 34, 35, 37, 45, 49, 52, 54, 66, 67, 80, 84, 87, 89, 90],31,),
    ([1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1],29,),
    ([10, 11, 13, 19, 19, 30, 33, 36, 40, 42, 44, 47, 49, 52, 53, 58, 66, 68, 72, 82, 87, 89, 90, 94],21,),
    ([-46, -35, 40, -76, -66, -47, 36, -82, -43, 12, -95, 54, 58, 82, -87, -17, -71, -97, -10, 4, 23, 86, -24],12,),
    ([0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],6,),
    ([88, 76, 16, 23, 40, 60, 73, 32, 15, 13, 5, 75, 74, 52, 77, 41, 53, 50, 15, 7, 40, 28, 32, 99, 15, 85],18,)
        ]
    filled_function_param = [
    ([3, 3, 6, 7, 9, 11, 15, 15, 17, 19, 21, 23, 26, 27, 37, 48, 48, 51, 53, 53, 59, 64, 69, 69, 70, 71, 72, 84, 93, 96],19,),
    ([66, -28, 6, 25, -65, 19, -86, -86, -90, 40, -62],8,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],26,),
    ([85, 84, 8, 36, 93, 76, 14, 54, 85, 86],9,),
    ([-90, -82, -80, -73, -67, -62, -62, -61, -58, -56, -56, -52, -50, -49, -49, -43, -43, -30, -26, -26, -15, -14, -13, -4, 10, 19, 20, 22, 26, 29, 34, 35, 37, 45, 49, 52, 54, 66, 67, 80, 84, 87, 89, 90],31,),
    ([1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1],29,),
    ([10, 11, 13, 19, 19, 30, 33, 36, 40, 42, 44, 47, 49, 52, 53, 58, 66, 68, 72, 82, 87, 89, 90, 94],21,),
    ([-46, -35, 40, -76, -66, -47, 36, -82, -43, 12, -95, 54, 58, 82, -87, -17, -71, -97, -10, 4, 23, 86, -24],12,),
    ([0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],6,),
    ([88, 76, 16, 23, 40, 60, 73, 32, 15, 13, 5, 75, 74, 52, 77, 41, 53, 50, 15, 7, 40, 28, 32, 99, 15, 85],18,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        f_filled(*(filled_function_param[i]))
        f_gold(*parameters_set)
        if parameters_set == filled_function_param[i]:
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))