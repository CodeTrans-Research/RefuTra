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
def f_gold ( string ) :
    string = string [ : : - 1 ]
    return string


def f_filled(str):
    n = len(str)
    for i in range(n//2):
        temp = str[i]
        str[i] = str[n - i - 1]
        str[n - i - 1] = temp
    return str

if __name__ == '__main__':
    param = [
    (['A', 'C', 'E', 'M', 'R', 'd', 'g', 'o'],),
    (['5', '7', '5', '2', '0', '8', '2', '4', '1', '5', '8', '0', '8', '8'],),
    (['0', '0', '0', '1', '1', '1', '1', '1', '1'],),
    (['p', 'M', 'h', 'O', 'b', 'I', 'P', 'X', 'V', 'z', 'Q', 'i', 'k', 'S', 'Z', 'j', 'O', 'q', 'f', 'A', 'Q', 'I', 'X', 'R', 'x', 's', 'a', 'Q', 'N', 'r', 'l', 'M', 'D', 'O', 'S', 'k', 'x', 'l', 'C', 'P'],),
    (['5'],),
    (['0', '0', '0', '0'],),
    (['L', 'R', 'W', 'g', 'l', 'w'],),
    (['0', '7', '9', '9', '9', '9', '9', '2', '9', '0', '3', '7', '8', '0', '2', '0', '9', '8', '7', '8', '0', '9', '1'],),
    (['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],),
    (['J', 'y', 'F', 'z', 'V', 'E', 'm', 'G', 'x', 'Y', 'G', 'F', 'J', 's', 'm', 'e', 'd', 'S', 'T', 'H', 'L', 'V', 'j', 't', 'B', 'u'],)
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
