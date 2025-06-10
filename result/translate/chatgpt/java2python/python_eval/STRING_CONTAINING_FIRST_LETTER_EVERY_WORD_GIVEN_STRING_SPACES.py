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
def f_gold ( str ) :
    result = ""
    v = True
    for i in range ( len ( str ) ) :
        if ( str [ i ] == ' ' ) :
            v = True
        elif ( str [ i ] != ' ' and v == True ) :
            result += ( str [ i ] )
            v = False
    return result


def f_filled(str):
    result = ""
    v = True
    for i in range(len(str)):
        if str[i] == ' ':
            v = True
        elif str[i] != ' ' and v == True:
            result += str[i]
            v = False
    return result

if __name__ == '__main__':
    param = [
    ('t a',),
    ('77 78 2 600 7',),
    ('011 10 10',),
    ('kV Co O iR',),
    ('2',),
    ('0 11',),
    ('Y sT wgheC',),
    ('58 824 6',),
    ('00 100 001 0111',),
    ('Q',)
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
