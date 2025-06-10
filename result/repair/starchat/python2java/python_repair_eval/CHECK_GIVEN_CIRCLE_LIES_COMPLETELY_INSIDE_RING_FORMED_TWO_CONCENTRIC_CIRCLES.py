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
import math

def f_gold ( r , R , r1 , x1 , y1 ) :
    dis = int ( math.sqrt ( x1 * x1 + y1 * y1 ) )
    return ( dis - r1 >= R and dis + r1 <= r )


def f_filled(r, R, r1, x1, y1):
        dis =  int(math.sqrt(x1*x1+y1*y1))
        return dis - r1 >= R and dis + r1 <= r

if __name__ == '__main__':
    param = [
    (3,1,1,2,2,),
    (400,1,10,74,38,),
    (1,400,10,74,38,),
    (61,40,2,50,0,),
    (60,49,68,77,71,),
    (88,10,69,71,26,),
    (60,79,92,29,38,),
    (26,88,75,84,10,),
    (33,65,57,21,61,),
    (70,57,77,52,87,)
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
