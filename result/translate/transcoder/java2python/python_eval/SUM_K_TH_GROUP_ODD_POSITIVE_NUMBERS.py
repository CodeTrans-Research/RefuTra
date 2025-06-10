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
def f_gold(k):
    cur = int((k * (k - 1)) + 1)
    sum = 0
    while k:
        sum += cur
        cur += 2
        k = k - 1
    return sum


def f_filled ( k ) :
    cur = ( k * ( k - 1 ) ) + 1
    sum = 0
    while k :
        sum += cur
        cur += 2
    return sum

if __name__ == '__main__':
    param = [
        (91,),
        (52,),
        (78,),
        (51,),
        (65,),
        (39,),
        (42,),
        (12,),
        (56,),
        (98,)
    ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success += 1
    print("#Results: %i, %i" % (n_success, len(param)))
