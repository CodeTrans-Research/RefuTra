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
def f_gold ( p ) :
    checkNumber = 2 ** p - 1
    nextval = 4 % checkNumber
    for i in range ( 1 , p - 1 ) :
        nextval = ( nextval * nextval - 2 ) % checkNumber
    if ( nextval == 0 ) : return True
    else : return False


def f_filled(p):
    checkNumber = pow(2, p) - 1
    nextval = 4 % checkNumber
    for i in range(1, p-1):
        nextval = (nextval * nextval - 2) % checkNumber
    return nextval == 0

if __name__ == '__main__':
    param = [
    (11,),
    (27,),
    (31,),
    (47,),
    (3,),
    (14,),
    (41,),
    (12,),
    (39,),
    (22,)
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

