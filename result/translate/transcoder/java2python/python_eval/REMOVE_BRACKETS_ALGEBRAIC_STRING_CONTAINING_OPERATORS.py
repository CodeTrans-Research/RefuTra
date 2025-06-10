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
def f_gold ( Str ) :
    Len = len ( Str )
    res = [ None ] * Len
    index = 0
    i = 0
    s = [ ]
    s.append ( 0 )
    while ( i < Len ) :
        if ( Str [ i ] == '+' ) :
            if ( s [ - 1 ] == 1 ) :
                res [ index ] = '-'
                index += 1
            if ( s [ - 1 ] == 0 ) :
                res [ index ] = '+'
                index += 1
        elif ( Str [ i ] == '-' ) :
            if ( s [ - 1 ] == 1 ) :
                res [ index ] = '+'
                index += 1
            elif ( s [ - 1 ] == 0 ) :
                res [ index ] = '-'
                index += 1
        elif ( Str [ i ] == '(' and i > 0 ) :
            if ( Str [ i - 1 ] == '-' ) :
                x = 0 if ( s [ - 1 ] == 1 ) else 1
                s.append ( x )
            elif ( Str [ i - 1 ] == '+' ) :
                s.append ( s [ - 1 ] )
        elif ( Str [ i ] == ')' ) :
            s.pop ( )
        else :
            res [ index ] = Str [ i ]
            index += 1
        i += 1
    return "".join(res)


def f_filled ( str ) :
    len ( str )
    res = [ ]
    index , i = 0 , 0
    s = Stack ( )
    s.push ( 0 )
    while i < len ( str ) :
        if str [ i ] == '+' :
            if s.pop ( ) == 1 :
                res.append ( '-' )
            if s.pop ( ) == 0 :
                res.append ( '+' )
        elif str [ i ] == '-' :
            if s.pop ( ) == 1 :
                res.append ( '+' )
            elif s.pop ( ) == 0 :
                res.append ( '-' )
        elif str [ i ] == '(' and i > 0 :
            if str [ i - 1 ] == '-' :
                x = ( s.pop ( ) == 1 )
                s.push ( x )
            elif str [ i - 1 ] == '+' :
                s.push ( s.pop ( ) )
        elif str [ i ] == ')' :
            s.pop ( )
        else :
            res.append ( str [ i ] )
        i += 1
    return ''.join ( res )

if __name__ == '__main__':
    param = [
    ('ggbsMvMZcMOVd',),
    ('384292670',),
    ('10000100',),
    ('fdHME',),
    ('09198832',),
    ('0011111011',),
    ('SnXwRS',),
    ('071',),
    ('01101',),
    ('xwmqxgBa',)
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

