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
def f_gold ( input , unlock_code ) :
    rotation = 0 ;
    while ( input > 0 or unlock_code > 0 ) :
        input_digit = input % 10 ;
        code_digit = unlock_code % 10 ;
        rotation += min ( abs ( input_digit - code_digit ) , 10 - abs ( input_digit - code_digit ) ) ;
        input = int ( input / 10 ) ;
        unlock_code = int ( unlock_code / 10 ) ;
    return rotation ;


def f_filled(input, unlock_code):
    rotation = 0
    while input > 0 or unlock_code > 0:
        input_digit = input % 10
        code_digit = unlock_code % 10
        rotation += min(abs(input_digit - code_digit), 10 - abs(input_digit - code_digit))
        input //= 10
        unlock_code //= 10
    return rotation

if __name__ == '__main__':
    param = [
    (71,46,),
    (90,65,),
    (28,84,),
    (41,23,),
    (32,58,),
    (39,82,),
    (33,58,),
    (89,32,),
    (50,51,),
    (92,77,)
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
