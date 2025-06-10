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
def f_gold ( a , b , mod ) :
    res = 0 ;
    a = a % mod ;
    while ( b > 0 ) :
        if ( b % 2 == 1 ) :
            res = ( res + a ) % mod ;
        a = ( a * 2 ) % mod ;
        b //= 2 ;
    return res % mod ;


def f_filled(a, b, mod):
  res = 0
  a = a % mod
  while b > 0:
    if b % 2 == 1:
      res = (res + a) % mod
    a = (a * 2) % mod
    b //= 2
  return res % mod

if __name__ == '__main__':
    param = [
    (99,75,40,),
    (11,4,41,),
    (51,37,23,),
    (49,51,88,),
    (9,34,30,),
    (90,85,55,),
    (19,96,41,),
    (17,96,37,),
    (54,3,51,),
    (5,69,60,)
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
