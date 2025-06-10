import sys
import math
import heapq
from queue import Queue# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( text , s ) :
    result = ""
    for i in range ( len ( text ) ) :
        char = text [ i ]
        if ( char.isupper ( ) ) :
            result += chr ( ( ord ( char ) + s - 65 ) % 26 + 65 )
        else :
            result += chr ( ( ord ( char ) + s - 97 ) % 26 + 97 )
    return result


def f_filled ( text, s ) :
        result = [ ]
        for i in range ( len ( text ) ) :
            if text [ i ].isupper ( ) :
                ch = chr ( ord ( text [ i ] ) + s - 65 ) % 26 + 65
                result.append ( ch )
            else :
                ch = chr ( ord ( text [ i ] ) + s - 97 ) % 26 + 97
                result.append ( ch )
        return ''.join ( result )

if __name__ == '__main__':
    param = [
    ('LsvbpcviVPwq',15,),
    ('35225904',2,),
    ('010010',36,),
    ('QnYd',44,),
    ('2571694',11,),
    ('101101011010',94,),
    ('jb',22,),
    ('928874',83,),
    ('11',93,),
    ('FbvbkMb',37,)
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
