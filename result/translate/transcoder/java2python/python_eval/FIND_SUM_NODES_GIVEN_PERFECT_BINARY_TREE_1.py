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

def f_gold ( l ) :
    leafNodeCount = math.pow ( 2 , l - 1 )
    sumLastLevel = 0
    sumLastLevel = ( ( leafNodeCount * ( leafNodeCount + 1 ) ) / 2 )
    sum = sumLastLevel * l
    return sum


def f_filled ( l ) :
    leaf_node_count = np.arange ( 2 , l - 1 )
    sum_last_level = 0
    sum_last_level = ( leaf_node_count * ( leaf_node_count + 1 ) ) / 2
    sum = sum_last_level * l
    return sum

if __name__ == '__main__':
    param = [
    (5,),
    (16,),
    (8,),
    (61,),
    (59,),
    (88,),
    (67,),
    (28,),
    (58,),
    (42,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if abs(1 - (0.0000001 + abs(f_gold(*parameters_set))) / (abs(f_filled(*parameters_set)) + 0.0000001)) < 0.001:
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))