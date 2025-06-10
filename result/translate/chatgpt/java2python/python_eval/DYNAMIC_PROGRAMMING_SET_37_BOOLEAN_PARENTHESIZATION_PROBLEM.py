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
def f_gold ( symb , oper , n ) :
    F = [ [ 0 for i in range ( n + 1 ) ] for i in range ( n + 1 ) ]
    T = [ [ 0 for i in range ( n + 1 ) ] for i in range ( n + 1 ) ]
    for i in range ( n ) :
        if symb [ i ] == 'F' :
            F [ i ] [ i ] = 1
        else :
            F [ i ] [ i ] = 0
        if symb [ i ] == 'T' :
            T [ i ] [ i ] = 1
        else :
            T [ i ] [ i ] = 0
    for gap in range ( 1 , n ) :
        i = 0
        for j in range ( gap , n ) :
            T [ i ] [ j ] = F [ i ] [ j ] = 0
            for g in range ( gap ) :
                k = i + g
                tik = T [ i ] [ k ] + F [ i ] [ k ] ;
                tkj = T [ k + 1 ] [ j ] + F [ k + 1 ] [ j ] ;
                if oper [ k ] == '&' :
                    T [ i ] [ j ] += T [ i ] [ k ] * T [ k + 1 ] [ j ]
                    F [ i ] [ j ] += ( tik * tkj - T [ i ] [ k ] * T [ k + 1 ] [ j ] )
                if oper [ k ] == '|' :
                    F [ i ] [ j ] += F [ i ] [ k ] * F [ k + 1 ] [ j ]
                    T [ i ] [ j ] += ( tik * tkj - F [ i ] [ k ] * F [ k + 1 ] [ j ] )
                if oper [ k ] == '^' :
                    T [ i ] [ j ] += ( F [ i ] [ k ] * T [ k + 1 ] [ j ] + T [ i ] [ k ] * F [ k + 1 ] [ j ] )
                    F [ i ] [ j ] += ( T [ i ] [ k ] * T [ k + 1 ] [ j ] + F [ i ] [ k ] * F [ k + 1 ] [ j ] )
            i += 1
    return T [ 0 ] [ n - 1 ]


def f_filled(symb, oper, n):
    F = [[0 for _ in range(n)] for _ in range(n)]
    T = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        F[i][i] = 1 if symb[i] == 'F' else 0
        T[i][i] = 1 if symb[i] == 'T' else 0
    
    for gap in range(1, n):
        for i in range(n-gap):
            j = i + gap
            T[i][j] = F[i][j] = 0
            for g in range(gap):
                k = i + g
                tik = T[i][k] + F[i][k]
                tkj = T[k+1][j] + F[k+1][j]
                if oper[k] == '&':
                    T[i][j] += T[i][k] * T[k+1][j]
                    F[i][j] += (tik * tkj) - (T[i][k] * T[k+1][j])
                elif oper[k] == '|':
                    F[i][j] += F[i][k] * F[k+1][j]
                    T[i][j] += (tik * tkj) - (F[i][k] * F[k+1][j])
                elif oper[k] == '^':
                    T[i][j] += F[i][k] * T[k+1][j] + T[i][k] * F[k+1][j]
                    F[i][j] += T[i][k] * T[k+1][j] + F[i][k] * F[k+1][j]
    
    return T[0][n-1]

if __name__ == '__main__':
    param = [
    ("TTFT", "|&^",4,),
    ("TFT", "^&",3,),
    ("TFF", "^|",3,),
    ("TTFT", "|||",4,),
    ("TTFT", "&&&",4,),
    ("TTFT", "&&^",4,),
    ("TTFT", "^&|",4,),
    ("TTFT", "^^^",4,),
    ("TTFT", "^||",4,),
    ("TTFT", "|^|",4,)
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
