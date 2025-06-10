import sys
import math
import heapq
from queue import Queue
# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( y , x ) :
    return ( y % pow ( 2 , x ) )


def f_filled(y, x):
    import math
    if (math.log(y) / math.log(2)) < x:
        return y
    if x > 63:
        return y
    return y % (1 << int(x))

if __name__ == '__main__':
    param = [
    (57,76,),
    (80,46,),
    (84,96,),
    (35,16,),
    (3,84,),
    (42,79,),
    (7,2,),
    (99,83,),
    (13,61,),
    (44,8,)
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
            if set([filledres,goldres]) == set([float("inf"),sys.maxsize]) or set([filledres,goldres]) <= set([float("-inf"),-sys.maxsize-1,-sys.maxsize]):
                n_success += 1
    print("#Results: %i, %i" % (n_success, len(param)))
