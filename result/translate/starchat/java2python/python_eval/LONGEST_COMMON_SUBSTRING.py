import sys
import math
import heapq
from queue import Queue# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( X , Y , m , n ) :
    LCSuff = [ [ 0 for k in range ( n + 1 ) ] for l in range ( m + 1 ) ]
    result = 0
    for i in range ( m + 1 ) :
        for j in range ( n + 1 ) :
            if ( i == 0 or j == 0 ) :
                LCSuff [ i ] [ j ] = 0
            elif ( X [ i - 1 ] == Y [ j - 1 ] ) :
                LCSuff [ i ] [ j ] = LCSuff [ i - 1 ] [ j - 1 ] + 1
                result = max ( result , LCSuff [ i ] [ j ] )
            else :
                LCSuff [ i ] [ j ] = 0
    return result


def f_filled(X, Y, m, n):
        LCStuff = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        result = 0
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    LCStuff[i][j] = 0
                elif X[i - 1] == Y[j - 1]:
                    LCStuff[i][j] = LCStuff[i - 1][j - 1] + 1
                    result = max(result, LCStuff[i][j])
                else:
                    LCStuff[i][j] = 0
        return result

if __name__ == '__main__':
    param = [
    (['A', 'D', 'E', 'E', 'L', 'L', 'T', 'r', 'x'],['D', 'F', 'H', 'O', 'g', 'o', 'u', 'v', 'w'],4,4,),
    (['9', '3', '4', '8', '7', '6', '3', '8', '3', '3', '5', '3', '5', '4', '2', '5', '5', '3', '6', '2', '1', '7', '4', '2', '7', '3', '2', '1', '3', '7', '6', '5', '0', '6', '3', '8', '5', '1', '7', '9', '2', '7'],['5', '5', '3', '7', '8', '0', '9', '8', '5', '8', '5', '1', '4', '4', '0', '2', '9', '2', '3', '1', '1', '3', '6', '1', '2', '0', '5', '4', '3', '7', '5', '5', '8', '1', '1', '4', '8', '1', '7', '5', '5', '4'],41,37,),
    (['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],35,29,),
    (['W', 'X', 'P', 'u', 's', 'k', 'O', 'y', 'Q', 'i', 't', 'z', 'F', 'f', 's', 'N', 'K', 'm', 'I', 'M', 'g', 'e', 'E', 'P', 'b', 'Y', 'c', 'O', ' ', 'G', 'F', 'x'],['e', 'R', 'P', 'W', 'd', 'a', 'A', 'j', 'H', 'v', 'T', 'w', 'x', 'I', 'd', 'o', 'z', 'K', 'B', 'M', 'J', 'L', 'a', ' ', 'T', 'L', 'V', 't', 'M', 'U', 'z', 'R'],31,18,),
    (['0', '1', '2', '4', '5', '7', '7', '7', '8', '8', '9', '9', '9'],['0', '0', '2', '2', '2', '3', '4', '6', '6', '7', '8', '9', '9'],12,8,),
    (['0', '0', '1'],['0', '0', '1'],1,1,),
    (['A', 'C', 'F', 'G', 'G', 'H', 'I', 'K', 'K', 'N', 'O', 'Q', 'R', 'V', 'V', 'W', 'Y', 'a', 'a', 'c', 'd', 'k', 'k', 'm', 'o', 'p', 't', 'u', 'y', 'y', 'y', 'z'],[' ', ' ', 'B', 'C', 'C', 'C', 'D', 'E', 'I', 'J', 'M', 'N', 'P', 'T', 'U', 'U', 'V', 'V', 'W', 'W', 'Y', 'b', 'c', 'e', 'i', 'o', 'p', 'r', 't', 'y', 'y', 'z'],21,23,),
    (['0', '0', '0', '2', '8', '3', '5', '1', '0', '7', '7', '9', '9', '4', '8', '9', '5'],['8', '5', '8', '7', '1', '4', '0', '2', '2', '7', '2', '4', '0', '8', '3', '8', '7'],13,12,),
    (['0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1'],['0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1'],9,9,),
    (['B', 'o', 'R', 'k', 'Y', 'M', 'g', 'b', 'h', 'A', 'i', 'X', 'p', 'i', 'j', 'f', 'V', 'n', 'd', 'P', 'T', 'U', 'f', 'G', 'M', 'W', 'g', 'a', 'C', 'E', 'v', 'C', ' '],['F', 'h', 'G', 'H', 'Q', 'Q', 'K', 'g', 'k', 'u', 'l', 'c', 'c', 'o', 'n', 'G', 'i', 'Z', 'd', 'b', 'c', 'b', 'v', 't', 'S', 't', 'P', 'A', 'K', 'g', 'G', 'i', 'm'],19,32,)
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
