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
def f_gold ( str ) :
    tmp = str + str
    n = len ( str )
    for i in range ( 1 , n + 1 ) :
        substring = tmp [ i : n ]
        if ( str == substring ) :
            return i
    return n


def f_filled ( str ) :
    tmp = str + str
    n = len ( str )
    for i in range ( 1 , n + 1 ) :
        substring = tmp [ i : i + len ( str ) ]
        if str == substring :
            return i
    return n

if __name__ == '__main__':
    param = [
    ('vdevdNdQSopPtj',),
    ('5',),
    ('100010101011',),
    ('tlDOvJHAyMllu',),
    ('06',),
    ('101',),
    ('DYgtU',),
    ('4',),
    ('00',),
    ('Dt',)
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
