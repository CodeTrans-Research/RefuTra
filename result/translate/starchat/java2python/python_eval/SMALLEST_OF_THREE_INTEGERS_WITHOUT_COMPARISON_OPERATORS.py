import sys
import math
import heapq
from queue import Queue# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( x , y , z ) :
    c = 0
    while ( x and y and z ) :
        x = x - 1
        y = y - 1
        z = z - 1
        c = c + 1
    return c


def f_filled(x, y, z):
        c = 0
        while x!= 0 and y!= 0 and z!= 0:
            x -= 1
            y -= 1
            z -= 1
            c += 1
        return c

if __name__ == '__main__':
    param = [
    (23,98,25,),
    (87,55,94,),
    (35,90,29,),
    (25,9,41,),
    (93,22,39,),
    (52,42,96,),
    (95,88,26,),
    (91,64,51,),
    (75,1,6,),
    (96,44,76,)
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
