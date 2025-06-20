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
    n = len ( str ) - 1
    i = n
    while ( i > 0 and str [ i - 1 ] <= str [ i ] ) :
        i -= 1
    if ( i <= 0 ) :
        return False
    j = i - 1
    while ( j + 1 <= n and str [ j + 1 ] <= str [ i - 1 ] ) :
        j += 1
    str = list ( str )
    temp = str [ i - 1 ]
    str [ i - 1 ] = str [ j ]
    str [ j ] = temp
    str = ''.join ( str )
    str [ : : - 1 ]
    return True

def f_filled(str):
    n = len(str) - 1
    i = n
    while i > 0 and str[i - 1] <= str[i]:
        i -= 1
    if i <= 0:
        return False
    j = i - 1
    while j + 1 <= n and str[j + 1] <= str[i - 1]:
        j += 1
    str[i - 1], str[j] = str[j], str[i - 1]
    str = "".join(str)
    str = str[::-1]
    return True

if __name__ == '__main__':
    param = [
    (['B', 'I', 'K', 'M', 'Q', 'Y', 'b', 'e', 'e', 't', 'x'],),
    (['7', '0', '2', '5', '1', '1', '4', '4', '8', '0', '2', '6', '4', '4', '0', '6', '7', '1', '7', '9', '8', '6', '1', '8', '3', '0', '6', '4', '4', '6', '3', '1', '3', '1', '9', '9', '4', '7', '4', '4', '3', '1', '4', '2', '9', '8', '1', '2', '4'],),
    (['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1'],),
    (['o', 'S', 'R', 'm', 'i', 'S', 'z', 'z', 'W', 'X', 'A', 'A', 'M', 'L', 'V', 'Q', 'F', 'i', ' ', 'i', 'G', 'D', 'T', 'a', 'm', 'S', 'N', 's', 'j', 'P', 'E', 'n', 'a', 'Q', 'm'],),
    (['0', '0', '0', '0', '1', '1', '1', '1', '1', '2', '2', '2', '2', '2', '3', '3', '3', '3', '3', '3', '3', '3', '4', '4', '4', '5', '5', '5', '5', '5', '5', '5', '5', '6', '7', '7', '8', '8', '8', '9', '9', '9', '9', '9'],),
    (['0', '0', '1', '0', '1', '0', '0'],),
    ([' ', 'B', 'D', 'D', 'E', 'E', 'G', 'J', 'J', 'K', 'L', 'L', 'L', 'M', 'N', 'N', 'P', 'Q', 'V', 'W', 'W', 'X', 'Y', 'a', 'b', 'b', 'd', 'f', 'h', 'i', 'j', 'j', 'k', 'k', 'l', 'm', 'm', 'm', 'n', 'p', 'r', 's', 'u', 'v', 'v', 'w', 'x'],),
    (['5', '4', '4', '7', '5', '5', '1', '8', '6', '6', '9', '9', '6', '6', '8', '7', '4', '0', '7', '3', '6', '0', '9'],),
    (['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],),
    (['q', 'a', 'U', 'N', 'V', 'v', 'U', 'R', 'x', 'i', 'S', 'N', 'V', 'V', 'j', 'r', 'e', 'N', 'M'],)
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
