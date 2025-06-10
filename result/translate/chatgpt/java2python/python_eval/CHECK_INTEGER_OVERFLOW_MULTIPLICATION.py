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
def f_gold ( a , b ) :
    if ( a == 0 or b == 0 ) :
        return False
    result = a * b
    if ( a == ( result // b ) ) :
        return False
    else :
        return True


def f_filled(a, b):
    if a == 0 or b == 0:
        return False
    result = a * b
    if a == result // b:
        return False
    else:
        return True

if __name__ == '__main__':
    param = [
    (37,80,),
    (10000000000,-10000000000,),
    (10000000000,10000000000,),
    (999999999,999999999,),
    (39,36,),
    (92,56,),
    (14,21,),
    (19,38,),
    (14,82,),
    (88,41,)
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

