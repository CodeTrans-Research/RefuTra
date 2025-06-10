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
    n = len ( str )
    C = [ [ 0 for i in range ( n ) ] for i in range ( n ) ]
    P = [ [ False for i in range ( n ) ] for i in range ( n ) ]
    j = 0
    k = 0
    L = 0
    for i in range ( n ) :
        P [ i ] [ i ] = True ;
        C [ i ] [ i ] = 0 ;
    for L in range ( 2 , n + 1 ) :
        for i in range ( n - L + 1 ) :
            j = i + L - 1
            if L == 2 :
                P [ i ] [ j ] = ( str [ i ] == str [ j ] )
            else :
                P [ i ] [ j ] = ( ( str [ i ] == str [ j ] ) and P [ i + 1 ] [ j - 1 ] )
            if P [ i ] [ j ] == True :
                C [ i ] [ j ] = 0
            else :
                C [ i ] [ j ] = 100000000
                for k in range ( i , j ) :
                    C [ i ] [ j ] = min ( C [ i ] [ j ] , C [ i ] [ k ] + C [ k + 1 ] [ j ] + 1 )
    return C [ 0 ] [ n - 1 ]


def f_filled(str):
        n = len(str)
        C = [[0 for _ in range(n)] for _ in range(n)]
        P = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            P[i][i] = True
            C[i][i] = 0
        for L in range(2, n + 1):
            for i in range(n - L + 1):
                j = i + L - 1
                if L == 2:
                    P[i][j] = (str[i] == str[j])
                else:
                    P[i][j] = (str[i] == str[j]) and P[i + 1][j - 1]
                if P[i][j] == True:
                    C[i][j] = 0
                else:
                    C[i][j] = min(C[i][j], C[i][k] + C[k + 1][j] + 1 for k in range(i, j))
        return C[0][n - 1]

if __name__ == '__main__':
    param = [
    ('ydYdV',),
    ('4446057',),
    ('0111',),
    ('keEj',),
    ('642861576557',),
    ('11111000101',),
    ('ram',),
    ('09773261',),
    ('1',),
    ('AVBEKClFdj',)
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
