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
import math

def f_gold ( n ) :
    l = int ( math.sqrt ( n ) )
    sq = l * l
    if ( sq == n ) :
        return l * 4
    else :
        row = int ( n / l )
        perimeter = 2 * ( l + row )
        if ( n % l != 0 ) :
            perimeter += 2
        return perimeter


def f_filled(n):
    l = int(n ** 0.5)
    sq = l * l
    
    if sq == n:
        return l * 4
    else:
        row = n // l
        perimeter = 2 * (l + row)
        
        if n % l != 0:
            perimeter += 2
        
        return perimeter

if __name__ == '__main__':
    param = [
    (45,),
    (80,),
    (54,),
    (48,),
    (83,),
    (68,),
    (32,),
    (20,),
    (68,),
    (66,)
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

