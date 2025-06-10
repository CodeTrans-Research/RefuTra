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
def f_gold ( n ) :
    while ( int ( n / 100 ) ) :
        last_digit = int ( n % 10 )
        n = int ( n / 10 )
        n += last_digit * 3
    return ( n % 29 == 0 )


def f_filled ( n ) :
    while n / 100 > 0 :
        last_digit = int ( n % 10 )
        n /= 10
        n += last_digit * 3
    return ( n % 29 == 0 )

if __name__ == '__main__':
    param = [
    (29,),
(0,),
(65,),
(1419,),
(54,),
(7,),
(44,),
(34,),
(1160,),
(29292,)
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

