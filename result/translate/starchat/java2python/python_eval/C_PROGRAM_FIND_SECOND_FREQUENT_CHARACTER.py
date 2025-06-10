import sys
import math
import heapq
from queue import Queue# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( str ) :
    NO_OF_CHARS = 256
    count = [ 0 ] * NO_OF_CHARS
    for i in range ( len ( str ) ) :
        count [ ord ( str [ i ] ) ] += 1
    first , second = 0 , 0
    for i in range ( NO_OF_CHARS ) :
        if count [ i ] > count [ first ] :
            second = first
            first = i
        elif ( count [ i ] > count [ second ] and count [ i ] != count [ first ] ) :
            second = i
    return chr ( second )


def f_filled(str):
        count = [0] * 256
        for i in range(len(str)):
            count[ord(str[i])] += 1
        first, second = 0, 0
        for i in range(256):
            if count[i] > count[first]:
                second = first
                first = i
            elif count[i] > count[second] and count[i]!= count[first]:
                second = i
        return chr(second)

if __name__ == '__main__':
    param = [
    ('SgUmIrEAB',),
    ('304',),
    ('0010',),
    ('VGC BeErLvQ',),
    ('0872',),
    ('00110001',),
    ('Lsqwm',),
    ('308998',),
    ('1000011',),
    ('XCEOs',)
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
