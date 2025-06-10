import sys
import math
import heapq
from queue import Queue# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( s ) :
    length = int ( s / 3 )
    s -= length
    breadth = s // 2
    height = s - breadth
    return int ( length * breadth * height )


def f_filled(s):
        length = s // 3
        s -= length * 3
        breadth = s // 2
        height = s - breadth
        return length * breadth * height

if __name__ == '__main__':
    param = [
    (8,),
    (96,),
    (96,),
    (96,),
    (12,),
    (95,),
    (72,),
    (81,),
    (42,),
    (13,)
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
