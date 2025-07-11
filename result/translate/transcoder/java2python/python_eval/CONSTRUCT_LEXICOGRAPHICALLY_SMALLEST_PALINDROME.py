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
def f_gold ( string , l ) :
    string = list ( string )
    i = - 1
    j = l
    while i < j :
        i += 1
        j -= 1
        if ( string [ i ] == string [ j ] and string [ i ] != '*' ) :
            continue
        elif ( string [ i ] == string [ j ] and string [ i ] == '*' ) :
            string [ i ] = 'a'
            string [ j ] = 'a'
            continue
        elif string [ i ] == '*' :
            string [ i ] = string [ j ]
            continue
        elif string [ j ] == '*' :
            string [ j ] = string [ i ]
            continue
        print ( "Not Possible" )
        return ""
    return ''.join ( string )


def f_filled ( str , len ) :
    i , j = 0 , len - 1
    for i in range ( j ) :
        if str [ i ] == str [ j ] and str [ i ] != '*' :
            continue
        elif str [ i ] == str [ j ] and str [ i ] == '*' :
            str [ i ] = 'a'
            str [ j ] = 'a'
            continue
        elif str [ i ] == '*' :
            str [ i ] = str [ j ]
            continue
        elif str [ j ] == '*' :
            str [ j ] = str [ i ]
            continue
        print ( "Not Possible" )
        return ""
    return str

if __name__ == '__main__':
    param = [
    (['A', 'B', 'C', 'G', 'I', 'L', 'L', 'O', 'O', 'P', 'Q', 'S', 'W', 'Y', 'c', 'd', 'e', 'f', 'f', 'i', 'm', 'm', 'o', 'q', 'v', 'w', 'x', 'x', 'y', 'z'],27,),
    (['3', '2', '3', '6', '8', '9', '0', '5', '0', '5', '8', '7', '9', '0', '3', '6', '9', '6', '2', '4', '2', '3', '1', '2', '7', '9', '1', '8', '8', '7', '1', '1', '6', '1'],30,),
    (['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],27,),
    (['z', 'v', 'B', 'Y', 'n', 'K', 'h', 'C', 'T', 'L', 'g'],7,),
    (['1', '2', '5', '6', '7'],4,),
    (['0', '0', '1', '0'],3,),
    (['D', 'n', 'r'],1,),
    (['0', '9', '9', '1', '2', '1', '5', '3', '7', '5', '9', '2', '4', '4', '8', '9', '6', '4', '2', '8', '8', '5', '5', '7', '1', '7', '6', '2', '2', '2', '3', '3', '7', '9'],24,),
    (['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],21,),
    (['E', 's', 'I', 'S', 'h', 'H', 'i', 'm', 'v', 'B'],6,)
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
