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
def f_gold ( s , n ) :
    s1 = s
    for i in range ( 1 , n ) :
        s += s1
    return s


def f_filled ( s , n ) :
    s1 = s
    for i in range ( 1 , n ) :
        s += s1
    return s

if __name__ == '__main__':
    param = [
    ('LPWsaI',41,),
    ('9037515104',72,),
    ('00100010010111',95,),
    ('SbwipuE',27,),
    ('574314109',5,),
    ('1101',70,),
    ('f',91,),
    ('068',50,),
    ('000011001',38,),
    ('BWbUtIkC',79,)
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
