import sys
import math
import heapq
from queue import Queue# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
import math

def f_gold ( n ) :
    count = 0
    if ( n % 2 == 0 ) :
        count = count + 1
        while ( n % 2 == 0 ) :
            n = int ( n / 2 )
    i = 3
    while ( i <= int ( math.sqrt ( n ) ) ) :
        if ( n % i == 0 ) :
            count = count + 1
            while ( n % i == 0 ) :
                n = int ( n / i )
        i = i + 2
    if ( n > 2 ) :
        count = count + 1
    return count


def f_filled(n):
        count = 0
        if n % 2 == 0:
            count += 1
            while n % 2 == 0:
                n /= 2
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                count += 1
                while n % i == 0:
                    n /= i
        if n > 2:
            count += 1
        return count

if __name__ == '__main__':
    param = [
    (99,),
    (33,),
    (50,),
    (17,),
    (18,),
    (69,),
    (23,),
    (18,),
    (94,),
    (16,)
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
